
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

# note on custom embed class to get around signature error
# https://stackoverflow.com/questions/77555461/facing-issue-while-running-chroma-from-documents-function

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
file_dict = {}
for x in range(len(batch["documents"])):
    # print(db.get()["metadatas"][x])
    doc = batch["metadatas"][x]
    #source = doc["source"]
    #print(doc)
    print(doc['file_name'])
    count += 1
    #break
    file_dict[doc['file_name']] = 1

print(count)    

print(file_dict)
print(len(file_dict))

sorted_dict = dict(sorted(file_dict.items()))
for key in sorted_dict:
    print(key)

print(len(sorted_dict))    

#print(batch['documents'] )

vector_store = ChromaVectorStore(chroma_collection=collection)
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
    Emodel="llama2",
    model="llama3",
    request_timeout=4000.0,
)



query_engine = index.as_query_engine(llm=llama)

print(
    query_engine.query(
        #"In the Wild Cards series who is Dr Tachyon's favourite person?"
        #"List me all the names of spaceships you can find in works by A. Bertram Chandler"
        #"List all the main character aces in the novel Aces Abroad"
        "Give me the names of all the lighthugger ships in works by Alastair Reynolds"
        #"List all the lighthuggers in the novel ABsolution Gap"
        "Tell me about Neville Clavain's appearances in the Revelation Space books and stories"
    )
)





