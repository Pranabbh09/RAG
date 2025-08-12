from langchain.text_splitter import CharacterTextSplitter
import warnings

warnings.filterwarnings("ignore")

def split_texts(documents, chunk_size: int = 1000, chunk_overlap: int = 0):
    """
    Splits the given documents into smaller text chunks using CharacterTextSplitter.
    
    Parameters:
        documents (list): A list of document objects.
        chunk_size (int): The maximum size of each chunk in characters. Default is 1000.
        chunk_overlap (int): The overlap between chunks in characters. Default is 0.
    
    Returns:
        List of text chunks.
    """
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(documents)
    return texts
