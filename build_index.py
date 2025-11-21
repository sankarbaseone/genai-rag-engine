# Script to build the index
import chromadb
import ollama
import os
from dotenv import load_dotenv

load_dotenv()

def get_knowledge_text(filepath="data/knowledge.txt"):
    with open(filepath, "r") as f:
        return f.read()

def create_vector_db(path="vector_store"):
    chroma = chromadb.PersistentClient(path=path)
    return chroma.get_or_create_collection("knowledge_base")

def get_embedding(text, model='nomic-embed-text'):
    response = ollama.embeddings(model=model, prompt=text)
    return response['embedding']

def add_document(collection, text, embedding, doc_id="doc1"):
    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[doc_id]
    )

def main():
    try:
        text = get_knowledge_text()
        collection = create_vector_db()
        embedding = get_embedding(text)
        add_document(collection, text, embedding)
        print("Vector store created successfully!")
    except Exception as e:
        print(f"Error creating vector store: {e}")

if __name__ == "__main__":
    main()
