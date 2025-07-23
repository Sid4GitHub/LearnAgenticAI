 # LearnAgenticAI

## Overview
**LearnAgenticAI** is a hands‑on repository designed to help you explore and build **agentic AI** applications using cutting‑edge tools and frameworks. Through code examples and tutorials, you’ll learn how to orchestrate long‑running, stateful AI agents capable of complex reasoning and task automation.

## Key Features
- **Agentic Workflows**  
  Build multi‑step AI agents that persist state, call external tools, and handle branching logic.
- **Ollama Integration**  
  Leverage Ollama as your local or hosted LLM runtime for fast, privacy‑preserving inference.
- **LangChain & LangGraph**  
  Compose and orchestrate agents with LangChain’s modular components, and unlock advanced graph‑based workflows with LangGraph.
- **Conda Environment**  
  Isolate dependencies and manage reproducible development environments with Conda.

## Prerequisites
- **Python:** ≥ 3.12.3  
- **Conda:** Anaconda or Miniconda installed  
- **Ollama:** Installed locally (see References)  
- **Git:** for cloning this repository

## Setup & Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your‑username/LearnAgenticAI.git
   cd LearnAgenticAI
 
2. **Create & activate Conda env**

   ```bash
   conda env create -f environment.yml
   conda activate learn‑agentic‑ai
   ```

3. **Install Ollama**
   Follow the official guide to install and configure Ollama for your platform.

4. **Run examples**

   * Navigate to any example folder (e.g., `examples/langgraph_react_agent/`)
   * Review the README there for usage instructions
   * Execute:

     ```bash
     python run_agent.py
     ```

## Repository Structure

```
├── examples/           # Self‑contained agent examples
│   ├── langchain/      # Basic LangChain agent
│   │   ├── notebooks/  # Jupyter notebooks
│   ├── langgraph/      # Stateful, graph‑based workflows
│   │   ├── notebooks/  # Jupyter notebooks
│   ├── ollama_demo/    # Inference with Ollama
│   └── mcp/            # MCP Server     
├── notebooks/          # Jupyter notebooks for exploration
├── .env                # load environment variable using dotenv
├── environment.yml     # Conda environment specification
└── README.md           # This file
```

## Getting Started

1. **Explore basic agents** in `examples/langchain_simple/` to understand prompt chaining.
2. **Advance to LangGraph** in `examples/langgraph_advanced/` to build cyclic, stateful workflows.
3. **Experiment with Ollama** in `examples/ollama_demo/` to see local LLM inference in action.
4. **Modify & Extend**: swap models, add tools, or integrate new memory backends.

## References

* **LangChain Docs:**
  [https://langchain.com/docs/](https://langchain.com/docs/)
* **LangGraph (Graph‑based Agents):**
  [https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
* **Ollama Docs:**
  [https://ollama.com/docs](https://ollama.com/docs)

Happy learning and building with Agentic AI! 🚀
