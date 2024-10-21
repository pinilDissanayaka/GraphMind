import streamlit as st
from graph import connect_graph
from secrects import setup_secrets

neo4j_url=None
neo4j_user_name=None
neo4j_password=None

st.set_page_config(page_title="GraphMind")

#app side bar
with st.sidebar:
    st.subheader("Upload the credentials.")
    
    neo4j_url = st.text_input("Neo4j URL", "bolt://localhost:7687")
    neo4j_user_name = st.text_input("Neo4j User Name", "neo4j")
    neo4j_password = st.text_input("Neo4j Password", "password", type="password")
    
    if neo4j_url and neo4j_user_name and neo4j_password:
        setup_secrets(neo4j_url, neo4j_user_name, neo4j_password)
        st.write("✅ Neo4j credentials saved")
    else:
        setup_secrets()
        st.write("✅ Neo4j credentials saved")
        
