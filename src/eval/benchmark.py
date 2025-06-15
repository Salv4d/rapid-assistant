from src.rag.vector_store import get_vectorstore

# 🔎 Queries de teste e o que esperamos encontrar nos chunks
test_cases = [
    {"query": "Embeddings são vetores?", "expected_substring": "representações numéricas"},
    {"query": "Chunking melhora a busca?", "expected_substring": "Chunks muito curtos"},
    {"query": "É útil usar metadados na busca?", "expected_substring": "melhora a precisão dos resultados"},
    {"query": "Chroma é melhor que FAISS?", "expected_substring": "Chroma"},
    {"query": "Como saber se minha busca vetorial está funcionando bem?", "expected_substring": "MRR > 0.7"}
]

vectordb = get_vectorstore()

print(f"{'Query':<55} | {'Encontrado no Top-3?':<18}")
print("-" * 80)

for case in test_cases:
    docs = vectordb.similarity_search(case["query"], k=3)
    joined_texts = " ".join(d.page_content for d in docs)
    hit = case["expected_substring"].lower() in joined_texts.lower()
    status = "✅ SIM" if hit else "❌ NÃO"
    print(f"{case['query']:<55} | {status:<18}")
