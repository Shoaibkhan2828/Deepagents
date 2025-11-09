# 🧠 Agentic Research Workflow using DeepAgents + LangChain  

This repository demonstrates an **Agentic Workflow** built using **DeepAgents (LangChain)** for automating academic research and literature synthesis.  
The system consists of two specialized sub-agents that collaborate to collect, analyze, and summarize research papers.  

---

## 🚀 Overview  

The goal of this project is to explore how **Agentic architectures** can streamline the research process — from information retrieval to structured synthesis.  

---

## 🧩 System Design  

**🔹 Research Agent**  
Retrieves and compiles relevant academic papers and resources using a custom retrieval tool.  

**🔹 Synthesis Agent**  
Extracts and organizes key insights such as:  
- Summary  
- Methods  
- Findings  
- Gaps  
- Future Work  

---

## 🔑 Key Takeaways  

1. **Modular Agent Design** enhances scalability — each sub-agent can be refined independently.  
2. **Well-defined task boundaries** improve output quality (defining *what* vs. *how* for each agent).  
3. **Synthesis accuracy** depends on prompt structure and context handoff between agents.  
4. **Future potential:** Integration of feedback loops and citation validation could enhance reliability for academic and industrial applications.  

---

## 💬 Conclusion  

This project reinforces the idea that **AI agents aren’t just tools — they’re collaborators in knowledge discovery.**  
Feel free to explore, adapt, or extend this workflow for your own research automation needs.  

---
## ⚙️ Installation and Running Instructions  

Follow these steps to set up and run the project locally.

---

### 1. Clone or Download the Repository  
### 2. Create and Activate a Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies

Install all required Python packages using the requirements.txt file:
```bash
pip install -r requirements.txt

4. Run the Streamlit Application

Launch the Streamlit app:
```bash
streamlit run app.py



## 🗂️ Project Structure  

