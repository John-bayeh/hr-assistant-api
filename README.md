# HR Assistant API

An AI-powered HR assistant backend built with Python, FastAPI, and Groq LLM.

## Features
- AI-powered HR question answering
- Ethiopian labor law knowledge
- Employee data analysis
- Salary insights by department

## Tech Stack
- Python 3.12
- FastAPI
- Groq LLM (LLaMA 3.3 70B)
- Pandas & NumPy
- Scikit-learn

## Live Demo
Frontend: https://hr-assistant-o1ktjq8e8-john-bayehs-projects.vercel.app

## API Endpoints
- `GET /` - Health check
- `POST /ask` - Ask HR questions

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Environment Variables
```
GROQ_API_KEY=your_groq_api_key
```