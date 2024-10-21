import os
import streamlit as st
from graph import connect_graph
from secrects import setup_neo4j_secrets, setup_llm_secrets

neo4j_url=None
neo4j_user_name=None
neo4j_password=None
graph=None

st.set_page_config(page_title="GraphMind")

#app side bar
with st.sidebar:
    st.subheader("Upload the credentials.")
    
    if "NEO4J_URL" and "NEO4J_USER_NAME" and "NEO4J_PASSWORD" in st.secrets:
        setup_neo4j_secrets()
    else:
        neo4j_url = st.text_input("Neo4j URL", "bolt://localhost:7687")
        neo4j_user_name = st.text_input("Neo4j User Name", "neo4j")
        neo4j_password = st.text_input("Neo4j Password", "password", type="password")
        
        if neo4j_url and neo4j_user_name and neo4j_password:
            setup_neo4j_secrets(neo4j_url=neo4j_url, neo4j_user_name=neo4j_user_name, neo4j_password=neo4j_password)

    if st.button("Connect to Neo4j"):
        graph = connect_graph()
        if graph:
            st.success("✅ Connected to Neo4j")
        else:
            st.error("❌ Unable to connect to Neo4j")
            
    if graph:
        if "GROQ_API_KEY" in st.secrets:
            setup_llm_secrets()
            st.success("✅ LLM setup is complete")
        else:
            groq_api_key = st.text_input("Groq API Key", "", type="password")

            if st.button("Setup LLM"):
                setup_llm_secrets(groq_api_key=groq_api_key)
                st.success("✅ LLM setup is complete")
