# NCERT Sound Chapter Q&A with Smart Agent

This project leverages Retrieval Augmented Generation (RAG) with Google's Gemini language model to provide accurate answers to questions about the NCERT Sound Chapter. Additionally, it features a smart agent capable of generating and downloading question papers based on the chapter content.

## Features

- *Question Answering:* Ask questions about the NCERT Sound Chapter and receive precise answers using the power of AI.
- *Question Paper Generation:* Generate custom question papers on the Sound chapter, with options to include answers.
- *PDF Download:* Download the generated question paper as a PDF file.
- *User-Friendly Interface:* Interact with the system through a simple web interface built with Streamlit.

## How it Works

1. *Document Loading:* The NCERT Sound Chapter PDF is loaded and processed.
2. *Text Splitting:* The document is split into smaller chunks for efficient embedding.
3. *Embedding & Vector Store:* Text chunks are embedded using HuggingFace sentence transformers and stored in a Chroma vector database.
4. *Query Processing:*
   - For factual questions, the system retrieves relevant information from the vector store using similarity search.
   - For question paper generation requests, the system uses Google Gemini to generate questions based on the entire chapter content.
5. *Answer Generation:* Google Gemini uses the retrieved context (or the entire chapter for question paper generation) to generate a comprehensive answer or a well-structured question paper.

## Technologies Used

- *Langchain:* Framework for building LLM applications.
- *ChromaDB:* Vector database for efficient similarity search.
- *FastAPI:* Web framework for building the backend API.
- *Streamlit:* Framework for creating the interactive web interface.
- *Google Generative AI:* Google Gemini powers the language understanding and generation capabilities.
- *HuggingFace Sentence Transformers:* For generating text embeddings.
- *Uvicorn:* ASGI server for running the FastAPI application.

## Setup

1. *Clone the Repository:*
   ```bash
   git clone https://your-repository-url.git
   cd your-repository-name

2. Install Dependencies:
    ```bash
   pip install -r requirements.txt

3. Set Up Environment Variables:
   * Create a `.env` file in the project root directory.
   * Add your Google API key:

   ```bash
   GOOGLE_API_KEY=your_api_key_here


 4. Run the FastAPI Backend:
    ```bash
    uvicorn main:app --reload

 5. Run the Streamlit App:
    ```bash
     streamlit run app.py

## Usage
 * Access the App: Open your web browser and navigate to http://localhost:8501.
 * Ask Questions: Enter your questions about the NCERT Sound Chapter in the text box and click "Submit."
 * Generate Question Paper: Click the "Generate Question Paper" button to create a question paper. You can choose to include answers.
 * Download: If you generated a question paper, click the "Download Question Paper" button to save it as a PDF.

*Important Notes*

- Replace https://your-repository-url.git and your-repository-name with your actual repository information.
- Make sure you have a valid Google API key and have set it up in the .env file.
