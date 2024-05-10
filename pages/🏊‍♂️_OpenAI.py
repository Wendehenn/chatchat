import streamlit as st

if "openai_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = ""

st.set_page_config(page_title="OpenAI Settings", page_icon="🤖",layout="wide")

st.title("OpenAI Settings")

openai_api_key= st.text_input("API Key",value=st.session_state["openai_api_key"],type="default")

save = st.button("Save")

if save:
    st.session_state["openai_api_key"]=openai_api_key

