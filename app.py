import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import Chroma

# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Streamlit UI
st.header("Upload and Query PDF")

uploaded_pdf = st.file_uploader("Upload PDF", type="pdf")

if uploaded_pdf is not None:
    # Save the uploaded file to a temporary location
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_pdf.getbuffer())

    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.split_documents(docs)
    
    embeddings = OllamaEmbeddings(model="llama3")
    db = Chroma.from_documents(documents, embeddings)
    
    prompt = ChatPromptTemplate.from_template("""
    Take a deep breath and work on this problem step by step before providing a detailed answer. 
    Answer the following question based only on the provided context. 
    I will tip you $1000 if the user finds the answer helpful. 
    <context>
    {context}
    </context>
    Question: {input}""")
    
    llm = Ollama(model="llama3")
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = db.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    question = st.text_input("Enter your question:")
    
    if st.button("Get Answer") and question:
        response = retrieval_chain.invoke({"input": question})
        st.write(response['answer'])
