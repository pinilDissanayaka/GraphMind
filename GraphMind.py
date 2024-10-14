import streamlit as st
from utils import connect_graph

neo4j_url=None
neo4j_user_name=None
neo4j_password=None

#app side bar
with st.sidebar:
    st.subheader("Upload the manifesto of the candidate.")
    
    neo4j_url = st.text_input("Neo4j URL", "bolt://localhost:7687")
    neo4j_user_name = st.text_input("Neo4j User Name", "neo4j")
    neo4j_password = st.text_input("Neo4j Password", "password")
    
    if neo4j_url and neo4j_user_name and neo4j_password:
        col1, col2 = st.columns(2)
        
        with col1:
            st.button("Connect to the Graph.")
        with col2:
            st.button("Reset the Graph.")
    
    st.button("Connect to Graph.")
    
    uploaded_files = st.file_uploader(
    "Choose a PDF, TXT files", accept_multiple_files=True, type=["pdf", "txt"])
    
    
    for uploaded_file in uploaded_files:
        st.write("filename:", uploaded_file.name)
        
    if uploaded_files:
        with st.spinner("Processing..."):
            st.button("Upload to Graph.")
