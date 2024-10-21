import os
import streamlit as st
from langchain.graphs import Neo4jGraph

def connect_graph(neo4j_url:str, neo4j_user_name:str, neo4j_password:str):
    try:
        graph=Neo4jGraph(url=neo4j_url,
                        password=neo4j_password,
                        username=neo4j_user_name)
        return graph

    except Exception as e:
        st.error(f"Unable to connect: {e}")

def clear_graph(graph : Neo4jGraph):
    pass