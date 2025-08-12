import google.generativeai as genai
import warnings

warnings.filterwarnings("ignore")

def query_vector_store(vectorstore, query: str, k: int = 1):
    """
    Queries the vector store to retrieve the most relevant document for the given query.

    Parameters:
        vectorstore: The vector store containing document embeddings.
        query (str): The natural language query.
        k (int): The number of top results to return. Default is 1.

    Returns:
        The most relevant document for the query.
    """
    retrieved_document = vectorstore.similarity_search(query, k=k)[0].page_content
    return retrieved_document

def get_gemini_response(query: str, context: str):
    """
    Mock function for getting a response from Google Gemini. 
    This function would normally integrate with Google Generative AI.

    Parameters:
        query (str): The user's query.
        context (str): The retrieved document to provide context.

    Returns:
        A mock response (or real response if integrated with Gemini API).
    """
    # Placeholder for an actual call to the Gemini API.
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f""" 
    Using the context given below answer the query.                             
    CONTEXT: {context}
    QUERY: {query}   
    Make the answers on point.                             
                                    """)
    return response.text
