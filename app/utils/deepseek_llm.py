import os
import requests
from dotenv import load_dotenv
import re

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"


def call_groq_deepseek(prompt, context="", model="deepseek-r1-distill-llama-70b"):
    """
    Call the DeepSeek model via Groq Cloud API to generate an answer given a prompt and optional context.
    Args:
        prompt (str): The user's question.
        context (str): Retrieved context from documents.
        model (str): Model name (default: deepseek-r1-distill-llama-70b)
    Returns:
        str: The generated answer from DeepSeek via Groq.
    """
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {prompt}"}
        ]
    }
    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[Groq API Error] {str(e)}"

def filter_think_tags(response):
    """
    Remove content within <think>...</think> tags from the response.
    """
    return re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL) 