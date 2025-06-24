import chromadb
from chromadb.config import Settings

# Use the same persistent path
PERSIST_DIR = r"C:\Users\Disha\Desktop\M.tech\autobook\chromadb_store"

client = chromadb.PersistentClient(
    path=PERSIST_DIR,
    settings=Settings(anonymized_telemetry=False)
)

collection = client.get_or_create_collection(name="chapters")

def get_chapter(chapter_id: str):
    result = collection.get(ids=[chapter_id])
    return result['documents'][0] if result['documents'] else "Not found."

if __name__ == "__main__":
    print("\n📚 Available Chapter IDs:")
    for item in collection.get()['ids']:
        print(f" - {item}")

    chapter_id = input("\nEnter Chapter ID: ").strip()
    chapter_text = get_chapter(chapter_id)
    print("\n📘 Chapter Content:\n")
    print(chapter_text)
