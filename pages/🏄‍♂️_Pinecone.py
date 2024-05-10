import streamlit as st

if "pinecone_api_key" not in st.session_state:
    st.session_state["pinecone_api_key"] = ""

if "pinecone_environment" not in st.session_state:
    st.session_state["pinecone_environment"] = ""

st.set_page_config(page_title="Pinecone Settings", page_icon="🤖",layout="wide")

st.title("Pinecone Settings")

pinecone_api_key = st.text_input("API Key",value=st.session_state["pinecone_api_key"],type="default")
pinecone_environment = st.text_input("Environment",value=st.session_state["pinecone_environment"],type="default")

save = st.button("Save")

if save:
    st.session_state["pinecone_api_key"]=pinecone_api_key
    st.session_state["pinecone_environment"]=pinecone_environment

