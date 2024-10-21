import os
import streamlit as st
from graph import connect_graph, create_graph, clear_graph
from file import load_uploaded_file, save_uploaded_file, transform_documents_to_graph, split_documents
from secrects import setup_secrets
from tempfile import TemporaryDirectory


st.set_page_config(page_title="GraphMind")

#app side bar
with st.sidebar:    
    if "NEO4J_URL" and "NEO4J_USER_NAME" and "NEO4J_PASSWORD" and "GROQ_API_KEY" in st.secrets:
        setup_secrets()
        st.success("✅ Credentials saved!")
        st.session_state['credentials_saved'] = True
    else:
        st.subheader("Upload the credentials.")
            
        neo4j_url = st.text_input("Neo4j URL", "bolt://localhost:7687")
        neo4j_user_name = st.text_input("Neo4j User Name", "neo4j")
        neo4j_password = st.text_input("Neo4j Password", "password", type="password")
        groq_api_key = st.text_input("Groq API Key", "", type="password")
        
        
        if st.button("Save Credentials", on_click=setup_secrets(neo4j_url=neo4j_url, neo4j_user_name=neo4j_user_name, neo4j_password=neo4j_password, groq_api_key=groq_api_key)):
            st.success("✅ Credentials saved!")
            st.session_state['credentials_saved'] = True
        else:
            st.warning("⚠️ Please enter valid credentials!")
            st.session_state['credentials_saved'] = False
            
            

if "credentials_saved" in st.session_state:
    if st.session_state['credentials_saved']:
        if "graph" not in st.session_state:
            graph = connect_graph()
            st.session_state['graph']=graph
                        
        upload_files = st.file_uploader("Upload File", type="pdf", accept_multiple_files=True)
        
        if upload_files:
            for upload_file in upload_files:
                st.write("File name: ", upload_file.name)
                
    
    if "graph" in st.session_state:
        if st.button("Create Graph"):
            with TemporaryDirectory(dir='/') as temp_dir:
                save_uploaded_file(temp_dir=temp_dir, uploaded_files=upload_files)
                load_uploaded_file(temp_dir=temp_dir)
                documents = load_uploaded_file(temp_dir=temp_dir)
                graph = create_graph(graph=st.session_state['graph'], graph_documents=documents)
                st.session_state['graph']=graph
                
                schema=graph.get_schema()
                st.write(schema)
        
        

