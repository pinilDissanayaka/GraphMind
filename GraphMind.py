import streamlit as st
from utils import connect_graph

#app side bar
with st.sidebar:
    st.subheader("Upload the manifesto of the candidate.")
    
    neo4j_url = st.text_input("Neo4j URL", "bolt://localhost:7687")
    neo4j_user = st.text_input("Neo4j User Name", "neo4j")
    neo4j_password = st.text_input("Neo4j Password", "password")
    
    st.button("Connect to Graph.")
    
    uploaded_files = st.file_uploader(
    "Choose a PDF, TXT files", accept_multiple_files=True, type=["pdf", "txt"])
    
    
    for uploaded_file in uploaded_files:
        st.write("filename:", uploaded_file.name)
        
    if uploaded_files:
        with st.spinner("Processing..."):
            st.button("Upload to Graph.")
