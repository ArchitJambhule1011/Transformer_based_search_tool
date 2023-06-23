import faiss
import math
import pickle
import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer
from utilities.utils import vector_search


st.set_page_config(layout="wide", page_title="Transformer based News Search Engine", page_icon="🔍", 
                   initial_sidebar_state="expanded")

@st.cache_data
def read_data(data=r'E:\Projects\Semantic search\Data\Precprocessed_data.csv'):
    return pd.read_csv(data)


@st.cache_data
def load_bert_model(name="distilbert-base-nli-stsb-mean-tokens"):
    return SentenceTransformer(name)


@st.cache_data
def load_index(path="models/faiss_index(2).pickle"):
    with open(path, "rb") as h:
        data = pickle.load(h)
    return faiss.deserialize_index(data)


def main():
    # Load data and models
    data = read_data()
    model = load_bert_model()
    faiss_index = load_index()

    st.title("Transformer based News Search Engine")

    # User search
    user_input = st.text_area("Search box")

    if user_input:
        D, I = vector_search([user_input], model, faiss_index)
        for id_ in I.flatten().tolist():
            f = data[data.id == id_]


            st.write(
                f"""**{f.iloc[0].original_title}**  
            **Date**: {f.iloc[0].year}  
            **Description**: {f.iloc[0].abstract}  
            **Link**
            {f.iloc[0].link}
            """
            )




if __name__ == "__main__":
    main()