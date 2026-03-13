import streamlit as st
import requests

st.title("Chat RAG Application")

# Login Form
if 'username' not in st.session_state:
    st.session_state.username = None

if st.session_state.username is None:
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        response = requests.post("http://localhost:8000/token", data={"username": username, "password": password})
        if response.status_code == 200:
            st.session_state.username = username
            st.success("Logged in successfully")
        else:
            st.error("Login failed")

# Chat Interface
if st.session_state.username:
    query = st.text_input("Ask a question:")
    if st.button("Submit"):
        response = requests.post("http://localhost:8000/chat/", json={"query": query})
        if response.status_code == 200:
            st.write(response.json()["answer"])
        else:
            st.write("Error fetching data from FastAPI")

    if st.button("Logout"):
        st.session_state.username = None
        st.success("Logged out successfully")
