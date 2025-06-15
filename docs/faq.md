# FAQ - Assistente Inteligente

---

### 🤖 Embeddings são vetores?

Sim. Embeddings são representações numéricas (vetores) que capturam o significado semântico de entradas como textos ou imagens. Cada embedding é um vetor, mas nem todo vetor é um embedding — o embedding tem um propósito semântico específico.

---

### 🔍 O que significa "chunkar" um documento?

"Chunkar" é dividir um documento em partes menores (chamadas chunks) para melhorar a indexação e recuperação.  
Chunks muito curtos perdem contexto. Chunks muito longos dificultam distinção semântica.  
O ideal geralmente é entre 200 e 400 tokens, com sobreposição de 10–20%.

---

### 🧠 Vale a pena usar metadados junto com embeddings?

Sim. Metadados como autor, tipo de documento ou categoria permitem aplicar filtros na busca vetorial.  
Combinar embeddings com metadados melhora a precisão dos resultados e reduz ruído.

---

### ⚙️ Chroma ou FAISS: qual o melhor banco vetorial?

Depende do caso:

- **Chroma:** melhor para projetos pequenos ou médios, com ótima integração com LangChain.
- **FAISS:** excelente performance com grandes volumes de dados, mas requer configuração manual.

Ambos são bons — escolha depende da sua stack e escala.

---

### 📊 Como saber se minha busca vetorial está funcionando bem?

Use métricas:

- **Precision@k** — quantos dos `k` resultados são realmente relevantes?
- **MRR (Mean Reciprocal Rank)** — qual a posição do primeiro resultado relevante?
- Resultados ideais:
  - MRR > 0.7
  - Precision@3 > 0.66
  - A resposta correta no top 5 da maioria dos testes.
