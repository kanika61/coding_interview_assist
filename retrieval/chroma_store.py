import chromadb
from chromadb.utils import embedding_functions

def retrieve_context(query: str, n_results: int = 3) -> str:
    client = chromadb.PersistentClient(path="./chroma_db")

    embed_fn = embedding_functions.OllamaEmbeddingFunction(
        url="http://localhost:11434/api/embeddings",
        model_name="nomic-embed-text"
    )

    collection = client.get_collection(
        name="dsa_concepts",
        embedding_function=embed_fn
    )

    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    docs = results["documents"][0]
    return "\n\n".join(docs)
