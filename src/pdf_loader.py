
from langchain.document_loaders import PyPDFLoader
import warnings

warnings.filterwarnings("ignore")

def load_pdf(file_path: str):
    """
    Loads a PDF document from the given file path using PyPDFLoader.
    
    Parameters:
        file_path (str): The path to the PDF file.
    
    Returns:
        List of documents loaded from the PDF.
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents
