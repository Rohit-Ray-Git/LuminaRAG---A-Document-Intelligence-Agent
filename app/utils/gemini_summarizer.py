import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def gemini_summarize_web_results(query, web_results):
    """
    Use Gemini to summarize web search results for a user query.
    Args:
        query (str): The user's question.
        web_results (str): The web search snippets.
    Returns:
        str: Gemini's summarized answer.
    """
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    prompt = f"""
    You are a helpful assistant. Given the following web search results, answer the user's question as accurately and concisely as possible.
    
    User Question: {query}
    
    Web Search Results:
    {web_results}
    """
    response = model.invoke(prompt)
    return response.content if hasattr(response, 'content') else str(response) 