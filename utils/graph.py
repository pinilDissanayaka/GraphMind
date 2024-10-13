from langchain.graphs import Neo4jGraph

def connect_graph(url:str, password:str, userName:str):
    graph=Neo4jGraph(url=url,
                     password=password,
                     username=userName)
    