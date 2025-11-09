# app.py
import streamlit as st
import json
import os
from dotenv import load_dotenv
from session_manager import SessionManager
from langchain_google_genai import ChatGoogleGenerativeAI
from deepagents import create_deep_agent
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.retrievers import ArxivRetriever
from model import SynthesisAgentModel,ResearchAgentModel,AggregatedModel
from extract import extract_json
load_dotenv()

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    verbose=True,
    api_key=os.getenv("api_key")
)

# Initialize session manager
if "session_manager" not in st.session_state:
    st.session_state.session_manager = SessionManager()

def relevant_paper(query: str, include_raw_content: bool = True) -> dict:
    """
    Fetches metadata and optionally full content of a relevant arXiv paper based on the query.
    Returns a dictionary with keys:
        - "Information on relevant document": metadata
        - "Content on relevant document": full text (optional)
    """
    retriever = ArxivRetriever(
        load_max_docs=1,
        get_full_documents=True,
    )
    docs = retriever.invoke(query)
    if not docs:
        return {}

    document = {"Information on relevant document": docs[0].metadata}
    if include_raw_content:
        document["Content on relevant document"] = docs[0].page_content
    return document

def run_deep_agent(query: str) -> dict:

    # Research sub-agent
    sub_research_prompt = """You are a dedicated researcher... Output ONLY valid JSON:
        {
        "Title": "....",
        "Authors": ["Author name 1", "Author name 2", "Author name 3"],
        "Summary": "..."
        }
        """


    research_sub_agent = {
        "name": "research-agent",
        "description": "Researcher agent",
        "system_prompt": sub_research_prompt,
        "tools": [relevant_paper],
        "input_variables": ["query"],
        "parsers": [JsonOutputParser(model=ResearchAgentModel)],
    }

    # Synthesis sub-agent
    synthesis_agent_prompt = """You are a scientific synthesis agent...
    Output ONLY valid JSON (no markdown, no commentary):
    {
      "Summary": "...",
      "Methods": "...",
      "Findings": "...",
      "Gaps_and_Future_Work": "..."
    }"""

    synthesis_sub_agent = {
        "name": "synthesis-agent",
        "description": "Summarizes findings",
        "system_prompt": synthesis_agent_prompt,
        "input_variables": ["document"],
        "parsers": [JsonOutputParser(model=SynthesisAgentModel)],
    }

    system_prompt = """
You are a scientific synthesis agent.

Input: a dict named "document" with:
{
  "Information on relevant document": {...},
  "Content on relevant document": "..."
}

Task: 
1. Extract Title, Authors, Summary from the document for research_sub_agent.
2. Summarize Methods, Findings, Gaps, and Future Work for synthesis_sub_agent.

Output ONLY a single JSON object:

{
  "research_sub_agent": {
    "Title": "...",
    "Authors": ["Author 1", "Author 2", "Author 3"],
    "Summary": "..."
  },
  "synthesis_sub_agent": {
    "Summary": "...",
    "Methods": "...",
    "Findings": "...",
    "Gaps_and_Future_Work": "..."
  }
}

Do NOT include any commentary, markdown, or extra text.
"""


    agent = create_deep_agent(
        tools=[relevant_paper],
        system_prompt=system_prompt,
        subagents=[research_sub_agent, synthesis_sub_agent],
        model=llm, response_format = AggregatedModel
    )

    result = agent.invoke({"messages": [{"role": "user", "content": query}]})
    print(result)
    return result
st.title("Research & Synthesis Agent")

query = st.text_input("Enter arXiv ID or research query", value="2505.10468")

if st.button("Run Agents"):
    if not query.strip():
        st.warning("Please enter a query!")
    else:
        st.info("Loading...")
        data = run_deep_agent(query)
        print("data")
        print(data)
        print("--------------------------------------------------------------------------------------")
        research_output, synthesis_output = extract_json(data)
      
        print("Research Agent Output:", research_output)
        print("--------------------------------------------------------------------------------------")
        print("Synthesis Agent Output:", synthesis_output)
        # Display outputs safely
        st.subheader("🔬 Research Agent Output")
        if research_output:
            # st.json now receives a valid dictionary
            st.json(research_output)

        else:
            st.warning("No structured output found for the Research Agent.")

        # 4. Display the synthesis output
        st.subheader("✍️ Synthesis Agent Output")
        if synthesis_output:
            st.json(synthesis_output)
        else:
            st.warning("No structured output found for the Synthesis Agent.")
        agent_response = {"research_output": research_output,"synthesis_output": synthesis_output}
        log_entry = {"user_query": query,"agent_response": agent_response}
        try:
            if "session_manager" in st.session_state and hasattr(st.session_state, 'session_manager'):
                st.session_state.session_manager.set_user_data("interaction_log", log_entry)
                
                # Call the save function to write the log.
                st.session_state.session_manager.save_log()
                st.toast("Log saved successfully!")
            else:
                # This warning helps in debugging if the session manager fails to initialize.
                st.warning("Session manager not found. Log could not be saved.")

        except Exception as e:
            st.error(f"An error occurred while saving the log: {e}")
