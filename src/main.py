from env_setup import configure_google_api
from pdf_loader import load_pdf
from text_splitter import split_texts
from embeddings import create_embeddings
from query_system import query_vector_store, get_gemini_response
import warnings

warnings.filterwarnings("ignore")

def main():
    # Step 1: Configure the environment with Google API
    configure_google_api()
    
    # Step 2: Load PDF Document
    pdf_path = "./data/ncert_sound_chap.pdf" 
    documents = load_pdf(pdf_path)
    print(f"Loaded {len(documents)} document(s)")

    # Step 3: Split the loaded documents into chunks
    text_chunks = split_texts(documents)
    print(f"Document split into {len(text_chunks)} chunk(s)")

    # Step 4: Create embeddings and initialize vector store
    vectorstore = create_embeddings(text_chunks)
    print(f"Vector store created with {len(text_chunks)} chunk(s)")

    # Step 5: Query the system and get a response
    query = input("Enter your query: ")
    retrieved_document = query_vector_store(vectorstore, query)
    
    # Step 6: Get the response from Google Gemini or a mock function
    response = get_gemini_response(query, retrieved_document)
    print("\nGenerated Response:")
    print(response)

if __name__ == "__main__":
    main()
