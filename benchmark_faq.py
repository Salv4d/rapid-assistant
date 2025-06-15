from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_fn = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

vectordb = Chroma(
    persist_directory="chroma_store",
    collection_name="faq",
    embedding_function=embedding_fn
)

test_cases = [
    {"query": "Embeddings são vetores?", "expected_substring": "representações numéricas"},
    {"query": "Chunking melhora a busca?", "expected_substring": "Chunks muito curtos"},
    {"query": "É útil usar metadados na busca?", "expected_substring": "melhora a precisão dos resultados"},
    {"query": "Chroma é melhor que FAISS?", "expected_substring": "Chroma"},
    {"query": "Como saber se minha busca vetorial está funcionando bem?", "expected_substring": "métricas"}
]

print(f"{'Query':<55} | {'Encontrado no Top-3?':<18}")
print("-" * 80)

for case in test_cases:
    docs = vectordb.similarity_search(case["query"], k=3)
    joined_texts = " ".join(d.page_content for d in docs)
    hit = case["expected_substring"].lower() in joined_texts.lower()
    status = "✅ SIM" if hit else "❌ NÃO"
    print(f"{case['query']:<55} | {status:<18}")
