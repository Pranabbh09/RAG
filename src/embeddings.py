from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import warnings

warnings.filterwarnings("ignore")

def create_embeddings(texts, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    """
    Creates embeddings for the provided texts using HuggingFace's sentence-transformers model.

    Parameters:
        texts (list): A list of text chunks.
        model_name (str): The HuggingFace model name to use for embedding. Default is 'all-MiniLM-L6-v2'.

    Returns:
        A vector store created using the Chroma library.
    """
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    vectorstore = Chroma.from_documents(
        texts, 
        embeddings,
        collection_name="ncert_sound_chap", 
        persist_directory="db") 
    return vectorstore
