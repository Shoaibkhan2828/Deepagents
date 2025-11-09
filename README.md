🧠 Agentic Research Workflow using DeepAgents + LangChain
This repository demonstrates an Agentic Workflow built using DeepAgents (LangChain) for automating academic research and literature synthesis.
The system consists of two specialized sub-agents that collaborate to collect, analyze, and summarize research papers.

🚀 Overview
The goal of this project is to explore how Agentic architectures can streamline the research process — from information retrieval to structured synthesis.

🧩 System Design
Research Agent:
Retrieves and compiles relevant academic papers and resources using a custom retrieval tool.
Synthesis Agent:
Extracts and organizes key insights.

🔑 Key Takeaways
Modular Agent Design enhances scalability — each sub-agent can be refined independently.
Well-defined task boundaries improve output quality (defining what vs. how for each agent).
Synthesis accuracy depends on prompt structure and context handoff between agents.
Future potential: Integration of feedback loops and citation validation could enhance reliability for academic and industrial applications.

🧭 Future Directions
Integrating human-in-the-loop validation
Improving citation accuracy
Extending to domain-specific corpora (e.g., healthcare, AI ethics, climate research)

💬 Conclusion
This project reinforces the idea that AI agents aren’t just tools — they’re collaborators in knowledge discovery.
Feel free to explore, adapt, or extend this workflow for your own research automation needs.

⚙️ How to Run the Streamlit App
Follow these steps to set up and run the project locally.
🧩 1. Clone or dowload the Repository 
🐍 2. Create and Activate a Virtual Environment
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

📦 3. Install Dependencies
Install all required Python packages using the requirements.txt file:
pip install -r requirements.txt

🚀 4. Run the Streamlit Application
Launch the Streamlit app:
streamlit run app.py
