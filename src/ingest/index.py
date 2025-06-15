import os
import shutil
from langchain_community.document_loaders import TextLoader
from src.rag.vector_store import (
    get_text_splitter,
    create_vectorstore_from_documents
)
from src.config import VECTORSTORE_PATH

shutil.rmtree(VECTORSTORE_PATH, ignore_errors=True)
os.makedirs(VECTORSTORE_PATH, exist_ok=True)

loader = TextLoader("docs/faq.md")
docs = loader.load()

splitter = get_text_splitter()
chunks = splitter.split_documents(docs)

create_vectorstore_from_documents(chunks)

print("FAQ indexed com sucesso.")
