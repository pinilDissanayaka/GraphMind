import streamlit as st

def setup_secrets(neo4j_url, neo4j_user_name, neo4j_password):
    st.secrets["neo4j_url"] = neo4j_url
    st.secrets["neo4j_user_name"] = neo4j_user_name
    st.secrets["neo4j_password"] = neo4j_password