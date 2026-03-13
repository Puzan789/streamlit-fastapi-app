import streamlit as st
import requests

st.title("Chat RAG Application")

query = st.text_input("Ask a question:")
if st.button("Submit"):
    response = requests.post("http://localhost:8000/chat/", json={"query": query})
    if response.status_code == 200:
        st.write(response.json()["answer"])
    else:
        st.write("Error fetching data from FastAPI")