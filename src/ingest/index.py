import os
import shutil

from langchain_community.document_loaders import PyMuPDFLoader, TextLoader

from src.config import VECTORSTORE_PATH
from src.rag.vector_store import create_vectorstore_from_documents, get_text_splitter

DOCS_DIR = "docs"


def load_all_documents_from_directory():
    """Loads all supported documents from the docs directory."""
    supported_loaders = {
        ".md": TextLoader,
        ".txt": TextLoader,
        ".pdf": PyMuPDFLoader,
    }

    documents = []
    for filename in os.listdir(DOCS_DIR):
        path = os.path.join(DOCS_DIR, filename)
        ext = os.path.splitext(filename)[1].lower()
        loader_class = supported_loaders.get(ext)

        if loader_class:
            try:
                loader = loader_class(path)
                documents.extend(loader.load())
            except Exception as e:
                print(f"Error loading '{filename}': {e}")
        else:
            print(f"Skipped unsupported file: '{filename}'")

    return documents


def main():
    shutil.rmtree(VECTORSTORE_PATH, ignore_errors=True)
    os.makedirs(VECTORSTORE_PATH, exist_ok=True)

    documents = load_all_documents_from_directory()
    if not documents:
        print("No valid documents found. Exiting.")
        return

    splitter = get_text_splitter()
    chunks = splitter.split_documents(documents)
    create_vectorstore_from_documents(chunks)

    print(f"{len(documents)} document(s) successfully indexed.")


if __name__ == "__main__":
    main()
