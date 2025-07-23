import os
import requests
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"  # Update if needed


def call_deepseek_r1(prompt, context=""):
    """
    Call the DeepSeek R1 API to generate an answer given a prompt and optional context.
    Args:
        prompt (str): The user's question.
        context (str): Retrieved context from documents.
    Returns:
        str: The generated answer from DeepSeek R1.
    """
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",  # Update to the correct model name if needed
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {prompt}"}
        ]
    }
    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[DeepSeek API Error] {str(e)}" 