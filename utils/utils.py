import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from utils.config import model_name, embedding_model


def get_llm(temperature:float):
    try:
        return ChatGroq(model=model_name,
                        temperature=temperature
                        )
    except Exception as e:
        st.exception(f"Unable to connect: \n {e.args}")
        

def get_embeddings():
    try:
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': False}

        embeddings = HuggingFaceEmbeddings(
            model_name=embedding_model,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
        
        return embeddings
    except Exception as e:
        st.exception(f"Unable to connect: \n {e.args}")
