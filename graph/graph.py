import os
from langchain.graphs import Neo4jGraph

def connect_graph():
    graph=Neo4jGraph(url=os.environ["neo4j_url"],
                     password=os.environ["neo4j_password"],
                     username=os.environ["neo4j_user_name"])
    return graph

def clear_graph():
    pass