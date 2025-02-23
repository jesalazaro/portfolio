import json
import os
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_google_vertexai import VertexAI
import PyPDF2
import vertexai
from vertexai.preview.generative_models import GenerativeModel

credentials = st.json.loads(st.secrets["GCP"]["credentials"])

GCP_CREDENTIALS_PATH = "/tmp/gcp_credentials.json"
with open(GCP_CREDENTIALS_PATH, "w") as f:
    json.dump(credentials, f)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GCP_CREDENTIALS_PATH

# Vertex AI initialization
PROJECT_ID = st.secrets["GCP"]["project_id"]
LOCATION = st.secrets["GCP"]["location"]
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Streamlit configuration
st.set_page_config(page_title="RAG with Vertex AI and GCP", layout="wide")

# Initialize LangChain components
@st.cache_resource
def initialize_langchain():
    embeddings = VertexAIEmbeddings(
        model_name="textembedding-gecko-multilingual",  # Fixed model name
        project=PROJECT_ID,
        location=LOCATION,
    )
    llm = VertexAI(
        model_name="gemini-pro",
        max_output_tokens=1024,
        temperature=0.1,
        project=PROJECT_ID,
        location=LOCATION,
    )
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key='answer'
    )
    return embeddings, llm, memory

# Extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Process document and create vector store
def process_document(text, embeddings):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
    )
    chunks = text_splitter.split_text(text)
    
    # Create vector store
    vectorstore = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )
    return vectorstore

# Initialize session state
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Main app
embeddings, llm, memory = initialize_langchain()

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    st.info("Processing document...")
    
    # Extract and process text
    text = extract_text_from_pdf(uploaded_file)
    vectorstore = process_document(text, embeddings)
    
    # Create conversation chain
    st.session_state.conversation = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        memory=memory,
        return_source_documents=True,
    )
    
    st.success("Document indexed. Ask a question!")

# Query interface
query = st.text_input("Ask a question about the document:")

if query and st.session_state.conversation:
    # Get response from conversation chain
    response = st.session_state.conversation({"question": query})
    
    # Display response
    st.write("### Answer:")
    st.write(response["answer"])
    
    # Update chat history
    st.session_state.chat_history.append({"role": "user", "content": query})
    st.session_state.chat_history.append({"role": "assistant", "content": response["answer"]})
    
    # Display source documents
    with st.expander("View source documents"):
        for doc in response["source_documents"]:
            st.write(doc.page_content)
            st.write("---")

# Display chat history
if st.session_state.chat_history:
    st.write("### Chat History")
    for message in st.session_state.chat_history[::-1]:
        with st.chat_message(message["role"]):
            st.write(message["content"])
