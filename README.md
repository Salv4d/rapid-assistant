# 🧠 Rapid Assistant

Rapid Assistant is a modular and extensible AI assistant powered by [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://www.langchain.com/), Retrieval-Augmented Generation (RAG), and Tool Calling.

Designed to be lightweight, provider-agnostic, and easily integrable with messaging platforms or APIs, Rapid Assistant provides a robust foundation for building intelligent agents with contextual reasoning and dynamic tool execution.

---

## ⚙️ Tech Stack

| Component     | Role                               |
| ------------- | ---------------------------------- |
| **Python**    | Main programming language          |
| **Poetry**    | Dependency and environment manager |
| **LangChain** | Tool abstraction and prompt logic  |
| **LangGraph** | Agent orchestration and state flow |
| **ChromaDB**  | Local vector database for RAG      |
| **dotenv**    | Env var loading (`.env`)           |

---

## 🚀 Getting Started

Clone the repository and install dependencies:

```bash
poetry install
poetry run python -m src.main
```

Create a `.env` file with any necessary API keys (e.g., for OpenAI, Gemini, etc.).

---

## 💡 Features

- ✅ Tool Calling with LLMs
- ✅ RAG (Retrieval-Augmented Generation) over Markdown documents
- ✅ Modular LangGraph state-based flow
- ✅ CLI interface for testing
- 🔜 Memory integration (short and long-term)
- 🔜 Human-in-the-loop design support
- 🔜 Ready for integration with APIs (e.g., Slack, Discord)

---

## 🗺️ Milestone Roadmap

| Milestone | Status | Description                 |
| --------- | ------ | --------------------------- |
| 1.1       | ✅     | Basic LLM interaction       |
| 1.2       | ✅     | RAG with ChromaDB           |
| 1.3       | ✅     | Tool Calling agent          |
| 2.1       | ✅     | Modular LangGraph structure |
| 2.2       | ✅     | Short-term memory           |
| 2.3       | 🔜     | Long-term user memory       |
| 2.4       | 🔜     | Human-in-the-loop support   |
| 3.x       | 🔜     | FastAPI + Slack integration |

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
