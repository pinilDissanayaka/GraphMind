import os
import streamlit as st

def setup_neo4j_secrets(neo4j_url=None, neo4j_user_name=None, neo4j_password=None):
    if not (neo4j_url and neo4j_user_name and neo4j_password):
        os.environ["NEO4J_URL"] = st.secrets["NEO4J_URL"]
        os.environ["NEO4J_USER_NAME"] = st.secrets["NEO4J_USER_NAME"]
        os.environ["NEO4J_PASSWORD"] = st.secrets["NEO4J_PASSWORD"]
    else:
        os.environ["NEO4J_URL"] = neo4j_url
        os.environ["NEO4J_USER_NAME"] = neo4j_user_name
        os.environ["NEO4J_PASSWORD"] = neo4j_password
        
def setup_llm_secrets(groq_api_key=None):
    if not groq_api_key:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    else:
        os.environ["GROQ_API_KEY"] = groq_api_key