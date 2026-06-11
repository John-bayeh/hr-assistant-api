from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME
from data_analyzer import get_company_summary

client = Groq(api_key=GROQ_API_KEY)

def ask_ai(question: str) -> str:
    try:
        company_data = get_company_summary()
        
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": f"""You are a professional HR assistant for an Ethiopian company.
You have access to real company data:
{company_data}
Use this data to answer questions accurately.
If asked about employees, salary, or performance — use the data above.
Be concise and professional."""},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"