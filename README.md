# 🧠 Rapid Assistant

Rapid Assistant is a modular and extensible AI assistant powered by [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://www.langchain.com/), Retrieval-Augmented Generation (RAG), Tool Calling, and Memory.

Designed to be lightweight, provider-agnostic, and easily integrable with messaging platforms or APIs, Rapid Assistant provides a robust foundation for building intelligent agents with contextual reasoning, user personalization, and dynamic tool execution.

---

## ⚙️ Tech Stack

| Component     | Role                                         |
| ------------- | -------------------------------------------- |
| **Python**    | Main programming language                    |
| **Poetry**    | Dependency and environment manager           |
| **LangChain** | Tool abstraction, prompt logic, and memory   |
| **LangGraph** | Agent orchestration and state flow           |
| **ChromaDB**  | Vector database for RAG and long-term memory |
| **dotenv**    | Env var loading (`.env`)                     |

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

- ✅ Tool Calling with LLMs (via LangChain tool bindings)
- ✅ RAG (Retrieval-Augmented Generation) using ChromaDB
- ✅ Modular LangGraph state-based agent architecture
- ✅ CLI interface for testing and development
- ✅ **Long-term memory** with semantic search and user-specific context
- ✅ Automatic preference recovery at session start
- ✅ Memory filtering via LLM (only stores relevant, structured preferences)
- 🔜 Human-in-the-loop design support
- 🔜 API-ready architecture (e.g., FastAPI + Slack integration)

---

## 🧠 Memory Design

- **Short-term memory**: Stored per session, used to build contextual prompts (via `get_history()`).
- **Long-term memory**: Stored in a dedicated ChromaDB collection, includes facts and preferences.
- **User profile**: Automatically loaded at the beginning of a session and injected into prompts.

Example stored preference:

```
The user prefers to receive answers in English with code examples and clear comments.
```

This is injected into system prompts to guide tone, format, and language.

---

## 🗺️ Milestone Roadmap

| Milestone | Status | Description                         |
| --------- | ------ | ----------------------------------- |
| 1.1       | ✅     | Basic LLM interaction               |
| 1.2       | ✅     | RAG with ChromaDB                   |
| 1.3       | ✅     | Tool Calling agent                  |
| 2.1       | ✅     | Modular LangGraph structure         |
| 2.2       | ✅     | Short-term memory                   |
| 2.3       | ✅     | Long-term user memory + RAG context |
| 2.4       | 🔜     | Human-in-the-loop support           |
| 3.x       | 🔜     | FastAPI + Slack integration         |

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
