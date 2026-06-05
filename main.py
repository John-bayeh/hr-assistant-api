from fastapi import FastAPI
from pydantic import BaseModel
from ai_service import ask_ai

app = FastAPI()

class Question(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "AI is running "}

@app.post("/ask")
def ask(question: Question):
    answer = ask_ai(question.text)
    return {"question": question.text, "answer": answer}