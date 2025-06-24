# versioning.py
import chromadb
from chromadb.config import Settings
import os

def save_version(text, chapter_num):
    persist_path = os.path.join(os.getcwd(), "chromadb_store")

    client = chromadb.PersistentClient(
        path=persist_path,
        settings=Settings(anonymized_telemetry=False)
    )

    collection = client.get_or_create_collection(name="chapters")
    doc_id = f"chapter_{chapter_num}"
    collection.add(
        documents=[text],
        ids=[doc_id],
        metadatas=[{"chapter_num": chapter_num}]
    )

    return doc_id
