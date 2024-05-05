
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
#from IPython.display import Markdown, display
import chromadb
from llama_index.llms.ollama import Ollama

embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

chroma_path = "/mnt/usb_mount/chroma/Calibre Books"
collection_name = "calibrebooks"

from chromadb.utils import embedding_functions
from chromadb import Documents, EmbeddingFunction, Embeddings
class MyEmbeddingFunction(EmbeddingFunction[Documents]):
    def __call__(self, input: Documents) -> Embeddings:
        sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="BAAI/bge-small-en-v1.5")
        embeddings = sentence_transformer_ef(input)
        return embeddings

custom = MyEmbeddingFunction()


print("LOAD CHROMA INDEX CHECK")

# load from disk
db2 = chromadb.PersistentClient(path=chroma_path)
#client = chromadb.PersistentClient(path="/path/to/save/to")
#collection = db2.get_collection(name=collection_name, embedding_function=embedding_model)
collection = db2.get_collection(name=collection_name, embedding_function=custom)

print(collection.count())

batch = collection.get(    include=["documents"])

print(len(batch))

for b in batch:
    print(b)

for d in batch['documenats']:
    print(d)

print(batch['documents'] )



