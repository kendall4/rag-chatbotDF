import gradio as gr
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings

Settings.llm = Ollama(model="llama3", request_timeout=120.0)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

PERSIST_DIR = "./storage"
storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()

def chat(message, history):
    response = query_engine.query(message)
    return response.response

demo = gr.ChatInterface(fn=chat, title="Dialogflow CX Assistant")
demo.launch()