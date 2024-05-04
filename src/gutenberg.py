
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
from llama_index.core import SimpleDirectoryReader

loader = SimpleDirectoryReader(
    input_dir=".test/library/jane-austen",
    required_exts=[".epub"],
    recursive=True,

)

documents = loader.load_data()

from llama_index.llms.ollama import Ollama

llama = Ollama(
    model="llama2",
    request_timeout=40.0,
)

query_engine = index.as_query_engine(llm=llama)

print(
    query_engine.query(
        "What are the titles of all the books available? Show me the context used to derive your answer."
    )
)



