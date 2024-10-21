import os
import streamlit as st
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def save_uploaded_file(temp_dir, uploaded_files):
    st.write("Saving file.")
    try:
        for uploaded_file in uploaded_files:
            save_dir=os.path.join(temp_dir, uploaded_file.name)
            
            with open(save_dir, "wb") as file:
                st.write("Saving file: ", uploaded_file.name)
                file.write(uploaded_file.read())
    
    except Exception as e:
        st.exception(f"Unable to save file: \n {e.args}")
        
        
def load_uploaded_file(temp_dir):
    st.write("Loading file.")
    try:
        pass