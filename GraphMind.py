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
    neo4j_password = st.text_input("Neo4j Password", "password", type="password")
    
    if neo4j_url and neo4j_user_name and neo4j_password:
        st.button("Connect to the Graph.", on_click=connect_graph(url=neo4j_url, password=neo4j_password, userName=neo4j_user_name))