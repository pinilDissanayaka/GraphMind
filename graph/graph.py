import os
import streamlit as st
from langchain.graphs import Neo4jGraph

def connect_graph():
    try:
        graph=Neo4jGraph(url=os.environ["NEO4J_URL"],
                        password=os.environ["NEO4J_PASSWORD"],
                        username=os.environ["NEO4J_USER_NAME"])
        return graph

    except Exception as e:
        st.error(f"Unable to connect: \n {e}")

def clear_graph(graph : Neo4jGraph):
    try:
        query = "MATCH (n) DETACH DELETE n"
        
        graph.query(query)
    except Exception as e:
        st.error(f"Unable to clear graph: \n {e}")