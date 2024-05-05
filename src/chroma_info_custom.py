
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

batch = collection.get()

print(len(batch))

for b in batch:
    print(b)

count = 0
for x in range(len(batch["documents"])):
    # print(db.get()["metadatas"][x])
    doc = batch["metadatas"][x]
    #source = doc["source"]
    print(doc)
    print(doc['file_name'])
    count += 1
    break

print(count)    


#print(batch['documents'] )

vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(
    vector_store,
    embed_model=embedding_model,
)

if 1 == 2:
    # Query Data from the persisted index
    query_engine = index.as_query_engine()
    response = query_engine.query("What did the author do growing up?")
    display(Markdown(f"<b>{response}</b>"))

print("SAMPLE QUERIES")

llama = Ollama(
    model="llama2",
    request_timeout=4000.0,
)

index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embedding_model,
)

query_engine = index.as_query_engine(llm=llama)

print(
    query_engine.query(
        "Please summarise the Christopher Anvil novel Pandora's Legions"
    )
)

print(
    query_engine.query(
        "What is the name of the main organisation in the Christopher Anvil novel?"
    )
)




