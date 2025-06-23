from src.rag.vector_store import get_rag_vectorstore

test_cases = [
    {
        "query": "Which house was Harry Potter sorted into?",
        "expected_substring": "Gryffindor"
    },
    {
        "query": "Who created the Walking Dead comics?",
        "expected_substring": "Robert Kirkman"
    },
    {
        "query": "What's the deeper meaning of the white whale?",
        "expected_substring": "obsession, the unknowable, fate"
    },
    {
        "query": "Explain the theme of Inception.",
        "expected_substring": "blurred line between what's real and what's imagined"
    },
    {
        "query": "Who directed Alien?",
        "expected_substring": "Ridley Scott"
    },
    {
        "query": "What's the story behind the One Ring?",
        "expected_substring": "forged by Sauron"
    },
    {
        "query": "What's the dystopia in 1984 about?",
        "expected_substring": "totalitarian regime"
    },
    {
        "query": "Who wrote Dracula?",
        "expected_substring": "Bram Stoker"
    },
    {
        "query": "What does The Matrix symbolize?",
        "expected_substring": "simulated reality"
    },
    {
        "query": "What is the plot of Arrival?",
        "expected_substring": "linguist, Dr. Louise Banks"
    }
]

vectordb = get_rag_vectorstore()

print(f"{'Query':<55} | {'Found in the Top-3?':<18}")
print("-" * 80)

for case in test_cases:
    docs = vectordb.similarity_search(case["query"], k=3)
    joined_texts = " ".join(d.page_content for d in docs)
    hit = case["expected_substring"].lower() in joined_texts.lower()
    status = "✅ YES" if hit else "❌ NO"
    print(f"{case['query']:<55} | {status:<18}")

