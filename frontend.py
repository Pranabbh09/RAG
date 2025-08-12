import streamlit as st
import requests
from fpdf import FPDF

# Set page configuration
st.set_page_config(page_title="NCERT Sound Chapter Q&A", page_icon="🔊")

# Custom CSS for purple color palette and button styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;  /* Light purple background */
    }
    .stButton button {
        background-color: #7a4fa3;  /* Darker purple for buttons */
        color: white;
    }
    .stTextInput input {
        background-color: #000000; /* Lighter purple for text input */
    }
    .sidebar .sidebar-content {
        background-color: #e0e0f0;  /* Even lighter purple for sidebar */
    }
    .generate-paper-button button {
        background-color: #9c67c3; /* Medium purple for the generate paper button */
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;  /* Add rounded corners */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
    }
    .generate-paper-button button:hover {
        background-color: #6a3593; /* Darker purple on hover */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Increase shadow on hover */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar content
with st.sidebar:
    st.header("About")
    st.write("This app lets you ask questions about the NCERT Sound Chapter and get accurate answers using AI.")
    st.write("You can also generate a question paper based on the chapter content.")
    st.write("**How it works:**")
    st.write("We've combined Retrieval Augmented Generation (RAG) with Google's powerful Gemini language model.")
    st.write("1. Your question is used to search relevant information from the NCERT textbook.")
    st.write("2. The AI then uses this context to generate a precise and informative answer.")
    st.write("**How to use:**")
    st.write("1. Enter your question in the text box and click 'Submit' to get an answer.")
    st.write("2. Click the 'Generate Question Paper' button to get a sample question paper.")

# Title and description
st.title("NCERT Sound Chapter Q&A")

# Query input
query = st.text_input("Enter your query:")

# Submit button for getting an answer
# Submit button for getting an answer
if st.button("Submit", key="answer_query_button"):
    if query:
        response = requests.post("http://127.0.0.1:8000/agent", json={"query": query})

        if response.status_code == 200:
            action = response.json()["action"]
            if action == "answer_from_vectordb":
                answer = response.json()["response"]
                st.markdown(f"**Answer:** {answer}")
            else:  # Handle generic responses or other actions
                st.write(response.json()["response"])
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    else:
        st.warning("Please enter a query.")

include_answers = st.checkbox("Include Answers in Question Paper")

# Button for generating question paper with custom styling and direct action
if st.button("Generate Question Paper", key="generate_paper_button"):
    response = requests.post("http://127.0.0.1:8000/agent", json={"query": "generate question paper", "include_answers": include_answers})

    if response.status_code == 200:
            action = response.json()["action"]
            question_paper = response.json()["response"]

            # Create PDF with UTF-8 encoding
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Encode the text to UTF-8 before adding it to the PDF
            encoded_text = question_paper.encode('latin-1', 'replace').decode('latin-1') 
            pdf.multi_cell(0, 10, encoded_text)

            pdf.output("question_paper.pdf")

            # Provide download link
            with open("question_paper.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()

            st.download_button(label="Download Question Paper",
                               data=PDFbyte,
                               file_name="question_paper.pdf",
                               mime='application/octet-stream')
    else:
        st.error(f"Error: {response.status_code} - {response.text}")