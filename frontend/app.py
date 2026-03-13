import streamlit as st
import requests

st.title("Streamlit and FastAPI")

response = requests.get("http://localhost:8000/")
if response.status_code == 200:
    st.write(response.json())
else:
    st.write("Error fetching data from FastAPI")