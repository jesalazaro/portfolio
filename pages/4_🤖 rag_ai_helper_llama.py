import streamlit as st
import os
import PyPDF2
import faiss
import numpy as np
from together import Together

# Load API key from Streamlit secrets
together_api_key = st.secrets["together_api_key"]
client = Together(api_key = together_api_key)

st.title("📄 RAG with Together AI (Llama 3.3 70B)")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to extract text from a PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    st.info("Processing document...")
    text = extract_text_from_pdf(uploaded_file)
    st.write(text)
    # Split text into chunks
    chunk_size = 500
    text_chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Convert text chunks into embeddings (placeholder for now)
    vector_dim = 768
    index = faiss.IndexFlatL2(vector_dim)
    embeddings = np.random.rand(len(text_chunks), vector_dim).astype('float32')  # Replace with actual embeddings
    index.add(embeddings)

    st.success("Document indexed. Ask a question!")

    query = st.text_input("Ask a question about the document:")

    if query:
        # Get the most relevant chunk (simple nearest neighbor search)
        query_embedding = np.random.rand(1, vector_dim).astype('float32')  # Replace with actual embedding of query
        _, nearest_idx = index.search(query_embedding, k=1)
        relevant_text = text_chunks[nearest_idx[0][0]]

        # Add chat history
        messages = [{"role": "system", "content": "You are an AI expert in document analysis."}]
        messages += st.session_state.chat_history  # Include previous messages
        messages.append({"role": "user", "content": f"Based on this text: {relevant_text}\n\nAnswer this question: {query}"})

        # Call Together AI for response
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages=messages,
            max_tokens=512,
            temperature=0.7,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1,
            stop=["<|eot_id|>", "<|eom_id|>"],
            stream=True
        )

        # Formatting streamed response
        formatted_response = ""
        for token in response:
            if hasattr(token, 'choices'):
                formatted_response += token.choices[0].delta.content + " "

        # Store the conversation in session state
        st.session_state.chat_history.append({"role": "user", "content": query})
        st.session_state.chat_history.append({"role": "assistant", "content": formatted_response.strip()})

    # Display chat history
    for message in st.session_state.chat_history[::-1]:
        with st.chat_message(message["role"]):
            st.write(message["content"])
