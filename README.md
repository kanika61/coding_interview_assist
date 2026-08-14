# Coding Interview Agent

AI-powered coding interview assistant for practicing data structures and algorithms.

## Overview

This project helps users prepare for coding interviews by:
- selecting DSA problems
- generating hints
- evaluating submitted solutions
- analyzing time and space complexity
- retrieving relevant algorithmic concepts using a lightweight RAG flow

The app runs locally and uses:
- Python
- Streamlit
- LangChain
- LangGraph
- Ollama
- ChromaDB

## Project structure

```text
coding_interview_assist/
├── README.md
└── coding_interview_agent/
    ├── agents/
    │   ├── __init__.py
    │   ├── complexity_agent.py
    │   ├── evaluator_agent.py
    │   └── hint_agent.py
    ├── retrieval/
    │   ├── __init__.py
    │   ├── chroma_store.py
    │   └── ingest.py
    ├── chroma_db/
    ├── graph.py
    ├── main.py
    ├── questions.py
    ├── scores.json
    ├── state.py
    ├── tracker.py
    ├── ui.py
    └── venv/
```

## Prerequisites

Before running the app, make sure you have:
- Python 3.10 or newer
- Ollama installed and running locally
- Access to pull the required Ollama models

## Setup

From the project root:

```bash
cd /Users/kprajapati/Documents/coding_interview_assist
```

Create and activate a virtual environment in the app directory:

```bash
cd coding_interview_agent
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install the dependencies:

```bash
pip install streamlit chromadb langgraph langchain-ollama langchain-core
```

## Ollama setup

If Ollama is not installed yet on macOS:

```bash
brew install ollama
```

Start the Ollama server:

```bash
ollama serve
```

Pull the required models in a second terminal:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

## Run the app

### 1) CLI version

From the project folder:

```bash
cd coding_interview_agent
python main.py
```

This starts the terminal-based experience where you can:
- paste a DSA problem
- ask for a hint
- evaluate your solution
- analyze complexity
- change the active problem

### 2) Streamlit UI version

From the project folder:

```bash
cd coding_interview_agent
streamlit run ui.py
```

Then open the URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Important notes

- Run the app from inside `coding_interview_agent` so that files like `ui.py` and `main.py` resolve correctly.
- The app expects a local Ollama instance running on `localhost:11434`.
- ChromaDB is used for local retrieval of DSA concept knowledge.
- The project is designed for local/offline experimentation and learning.

## How it works

The app follows this workflow:

1. A question is selected from the built-in list in `questions.py`
2. The problem text is used to retrieve relevant DSA concepts from ChromaDB
3. The user enters their current code
4. A LangGraph workflow routes the request to the correct agent:
   - `hint`
   - `evaluator`
   - `complexity`
5. The selected agent calls Ollama through LangChain and returns the generated response

## Data storage

The app stores usage history in a local JSON file:

```text
coding_interview_agent/scores.json
```

It logs entries such as date, problem title, intent, verdict, and language.

## License

This project is intended for educational and personal use.
