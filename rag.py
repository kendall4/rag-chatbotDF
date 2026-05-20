from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
import os

# Use local Ollama instead of OpenAI
Settings.llm = Ollama(model="llama3", request_timeout=120.0)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

PERSIST_DIR = "./storage"

if not os.path.exists(PERSIST_DIR):
    # First run - build and save the index
    print("Building index for the first time...")
    documents = SimpleDirectoryReader("/Users/kendall/Documents/rag-chatbot/data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=PERSIST_DIR)
    print("Index saved!")
else:
    # Already built - just load it
    print("Loading existing index...")
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)
    print("Index loaded!")

query_engine = index.as_query_engine()

while True:
    question = input("\nAsk a question (or type 'quit' to exit): ")
    if question.lower() == "quit":
        break
    response = query_engine.query(question)
    print(f"\n{response}")