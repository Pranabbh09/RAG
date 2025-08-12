from fastapi import FastAPI
from src.env_setup import configure_google_api
from src.pdf_loader import load_pdf
from src.text_splitter import split_texts
from src.embeddings import create_embeddings
from src.query_system import query_vector_store, get_gemini_response
import google.generativeai as genai
from pydantic import BaseModel

# Initialize API Configuration
configure_google_api()

# Load and process the PDF document
pdf_path = "data/ncert_sound_chap.pdf" 
documents = load_pdf(pdf_path)

# Split the loaded documents into chunks
text_chunks = split_texts(documents)

# Create embeddings and initialize vector store
vectorstore = create_embeddings(text_chunks)

app = FastAPI()

class Query(BaseModel):
    query: str

def should_use_vectordb(query: str) -> bool:
    """Determines if the VectorDB should be used based on the query."""
    # Simple check for greetings or generic phrases
    greetings = ["hello", "hi", "hey", "how are you", "what's up"]
    if any(greeting in query.lower() for greeting in greetings):
        return False
    # You can add more sophisticated logic here if needed
    return True

def generate_question_paper(include_answers: bool = False):
    """Generates a question paper based on the loaded document."""
    all_text = " ".join([doc.page_content for doc in documents])
    instruction = f"Generate a question paper with 5 questions (including a mix of multiple-choice, short answer, and long answer questions) based on the following text: {all_text}"
    if include_answers:
        instruction += " Also include the answers to the questions."
    else: instruction += " Also don't include the answers to the questions."
    model = genai.GenerativeModel('gemini-1.5-flash') 
    response = model.generate_content(instruction)
    return response.text

@app.post("/agent")
def handle_query(query: Query):
    if should_use_vectordb(query.query):
        retrieved_document = query_vector_store(vectorstore, query.query)
        response = get_gemini_response(query.query, retrieved_document)
        return {"action": "answer_from_vectordb", "response": response}
    elif "question paper" in query.query.lower() or "generate questions" in query.query.lower():
        question_paper = generate_question_paper(include_answers=query.include_answers)
        return {"action": "generate_question_paper", "response": question_paper}
    else:
        return {"action": "generic_response", "response": "Hello there! How can I help you today?"}