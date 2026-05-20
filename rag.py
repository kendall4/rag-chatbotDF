from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings

# Point to your PDFs
documents = SimpleDirectoryReader("/Users/kendall/Documents/rag-chatbot/data").load_data()
# Use local Ollama instead of OpenAI
Settings.llm = Ollama(model="llama3", request_timeout=120.0)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

# Build the index from your documents
index = VectorStoreIndex.from_documents(documents)

# Create a chat engine
query_engine = index.as_query_engine()

# Ask a question
while True:
    question = input("\nAsk a question (or type 'quit' to exit): ")
    if question.lower() == "quit":
        break
    response = query_engine.query(question)
    print(f"\n{response}")