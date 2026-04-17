# folder.py

from sentence_transformers import SentenceTransformer
import numpy as np

# Dummy Endee client (replace with actual Endee import)
# from endee import EndeeClient

class EndeeVectorDB:
    def __init__(self):
        # Load embedding model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Initialize storage (temporary in-memory)
        self.documents = []
        self.vectors = []
        
        # Replace this with real Endee connection
        # self.client = EndeeClient(api_key="YOUR_API_KEY")

    # 🔹 Convert text → vector
    def embed_text(self, text):
        return self.model.encode(text)

    # 🔹 Add documents to DB
    def add_documents(self, docs):
        for doc in docs:
            vector = self.embed_text(doc)
            self.documents.append(doc)
            self.vectors.append(vector)

            # Real Endee Example:
            # self.client.insert(vector=vector, metadata={"text": doc})

    # 🔹 Search similar docs
    def search(self, query, top_k=3):
        query_vector = self.embed_text(query)

        similarities = []
        for i, vec in enumerate(self.vectors):
            score = np.dot(query_vector, vec) / (
                np.linalg.norm(query_vector) * np.linalg.norm(vec)
            )
            similarities.append((score, self.documents[i]))

        # Sort by similarity
        similarities.sort(reverse=True, key=lambda x: x[0])

        return [doc for _, doc in similarities[:top_k]]

        # Real Endee Example:
        # results = self.client.search(query_vector, top_k=top_k)
        # return [r.metadata["text"] for r in results]
