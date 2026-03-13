from fastapi import FastAPI
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI

app = FastAPI()

# Initialize the vector store and QA chain
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.load_local("./faiss_index", embeddings)
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=vectorstore.as_retriever())

@app.post("/chat/")
async def chat(query: str):
    answer = qa.run(query)
    return {"answer": answer}