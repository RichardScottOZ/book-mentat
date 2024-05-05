from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
#from IPython.display import Markdown, display
import chromadb
from llama_index.llms.ollama import Ollama

embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

chroma_path = "/mnt/usb_mount/chroma/Calibre Books"
collection = "calibrebooks"

print("LOAD CHROMA INDEX CHECK")

# load from disk
db2 = chromadb.PersistentClient(path=chroma_path)
chroma_collection = db2.get_or_create_collection(collection)
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(
    vector_store,
    embed_model=embedding_model,
)

db = db2

print(db.get().keys())
print(len(db.get()["ids"]))

# Print the list of source files
for x in range(len(db.get()["ids"])):
    # print(db.get()["metadatas"][x])
    doc = db.get()["metadatas"][x]
    source = doc["source"]
    print(source)
