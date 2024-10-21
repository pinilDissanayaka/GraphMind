import os
import streamlit as st
from graph import connect_graph
from secrects import setup_secrets


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
        st.file_uploader("UPload File")
    

