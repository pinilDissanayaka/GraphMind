import os
import streamlit as st
from langchain.graphs import Neo4jGraph

def connect_graph():
    try:
        graph=Neo4jGraph(url=os.environ["neo4j_url"],
                        password=os.environ["neo4j_password"],
                        username=os.environ["neo4j_user_name"])
        return graph
    except Exception as e:
        st.error(f"Error: {e}")

def clear_graph():
    pass