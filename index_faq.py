import shutil
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

# Limpa o db
shutil.rmtree("chroma_store", ignore_errors=True)

# Carrega e divide o FAQ
loader = TextLoader("docs/faq.md")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Embedding
embedding_fn = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}  # mude para "cuda" se tiver GPU
)

# Cria e persiste base Chroma
Chroma.from_documents(
    documents=chunks,
    embedding=embedding_fn,
    persist_directory="chroma_store",
    collection_name="faq"
)

print("FAQ indexed com sucesso.")
