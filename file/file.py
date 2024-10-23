import os
import streamlit as st
from utils.utils import get_embeddings, get_llm
from langchain_community.document_loaders import PyPDFLoader, TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_experimental.graph_transformers import LLMGraphTransformer


def save_uploaded_file(temp_dir, uploaded_files):
    try:
        saved_files=[]
        for uploaded_file in uploaded_files:
            save_dir=os.path.join(temp_dir, uploaded_file.name)
            
            with open(save_dir, "wb") as file:
                file.write(uploaded_file.read())
                saved_files.append(uploaded_file.name)
        return saved_files
    
    except Exception as e:
        st.exception(f"Unable to save file: \n {e.args}")
        
        
def load_uploaded_file(temp_dir):
    try:
        loader = DirectoryLoader(temp_dir, glob="**/*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()
        return documents
    except Exception as e:
        st.exception(f"Unable to load file: \n {e.args}")
        
        
def split_documents(documents):
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=500
        )
        split_documents = text_splitter.split_documents(documents)
        return split_documents
    except Exception as e:
        st.exception(f"Unable to split documents: \n {e.args}")
        
def transform_documents_to_graph_documents(split_documents):

    try:
        transformer = LLMGraphTransformer(llm=get_llm(0.7))
        graph_documents = transformer.convert_to_graph_documents(split_documents)
        
        return graph_documents
    except Exception as e:
        st.exception(f"Unable to transform documents: \n {e.args}")