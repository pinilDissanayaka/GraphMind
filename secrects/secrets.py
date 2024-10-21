import os
import streamlit as st

def setup_secrets(neo4j_url=None, neo4j_user_name=None, neo4j_password=None, groq_api_key=None):
    if neo4j_url or neo4j_user_name or neo4j_password:
        os.environ["neo4j_url"] = st.secrets["neo4j_url"]
        os.environ["neo4j_user_name"] = st.secrets["neo4j_user_name"]
        os.environ["neo4j_password"] = st.secrets["neo4j_password"]
        os.environ["groq_api_key"] = st.secrets["groq_api_key"]
    else:
        os.environ["neo4j_url"] = neo4j_url
        os.environ["neo4j_user_name"] = neo4j_user_name
        os.environ["neo4j_password"] = neo4j_password
        os.environ["groq_api_key"] = groq_api_key