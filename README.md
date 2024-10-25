# 🌐 GraphMind
GraphMind transforms static PDF documents into interactive knowledge graphs using cutting-edge AI. Upload documents, extract entities and relationships, and interact with the knowledge graph in real-time through natural language queries. Powered by LLaMA 3.1 70B and Google Generative AI embeddings for unmatched accuracy in information extraction and querying.

## ✨ Features
- 📄 PDF-to-Knowledge Graph: Upload a PDF and extract key entities (people, places, organizations) and relationships (hierarchies, interactions) using AI models.
- 🧠 LLaMA 3.1 70B-Powered Entity & Relationship Extraction: Leverages the powerful LLaMA 3.1 model for accurate extraction.
- 🌍 Google Generative AI Embeddings: Advanced contextual understanding with Google GenAI embeddings.
- ⚡ Real-Time GraphRAG: Ask questions in plain English and get answers through real-time interaction with a Neo4j graph database.
- 🛠️ Modular & Configurable: Set up your OpenAI, Google GenAI, and Neo4j credentials easily.
- 💬 Natural Language Interface: Query the graph using everyday language for simple and powerful interactions.
- 🔗 Extensible: Future-proof design, ready to handle multiple documents, enhanced conversational querying, and more.
- 🖼️ Graph Visualization (Coming Soon): Intuitive visual representations of the extracted graphs.

## 🔧 Tech Stack
- Backend: Python, Neo4j, LangChain, LLaMA 3.1 70B, Google GenAI Embeddings
- Frontend: Streamlit 🖥️
- Query Language: Cypher for graph queries
- Graph Visualization : D3.js, NetworkX

## 🚀 Installation
### Prerequisites
1. 🐍 Python 3.8+
2. 🧑‍💻 Neo4j (Installed and running)
3. 🔑 Groq API Key (LLaMA 3.1 70B)
4. 🔑 Google Cloud API Key (Google Generative AI embeddings)

### Steps
1. Clone the repository:
```
git clone https://github.com/your-username/GraphMind.git
cd GraphMind
```

2. Install required dependencies:
```
pip install -r requirements.txt
```

3. Run the app with Streamlit:
```
streamlit run GraphMind.py
```

## 💡 Usage
1. Upload PDF: Navigate to the Streamlit app at localhost:8501 and upload a PDF. GraphMind will begin extracting entities and relationships.
2. Ask Questions: Use the natural language query feature to explore the knowledge graph.
3. Visualize (Coming Soon): Visual exploration of your knowledge graph is on the way!

## 🔮 Future Enhancements
- 🖼️ Graph Visualization: Explore graphs visually with a user-friendly interface.
- 🗣️ Conversational Interactions: Engage in multi-turn conversations with your knowledge graph.
- 📚 Multi-Document Support: Query across multiple documents for deeper insights.

## 🤝 Contributing
We welcome contributions! Please submit issues or pull requests to help improve GraphMind.

## 📄 License
This project is licensed under the MIT License.
