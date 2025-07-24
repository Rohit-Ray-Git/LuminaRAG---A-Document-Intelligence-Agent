import requests

def duckduckgo_search(query, max_results=5):
    """
    Perform a DuckDuckGo search and return a summary of the top results.
    Args:
        query (str): The search query.
        max_results (int): Number of results to return.
    Returns:
        str: Concatenated snippets from the top results.
    """
    url = f"https://duckduckgo.com/html/?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    snippets = []
    if response.status_code == 200:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all("a", class_="result__a", limit=max_results)
        for result in results:
            snippet = result.get_text()
            link = result.get("href")
            snippets.append(f"- {snippet} ({link})")
    return "\n".join(snippets) if snippets else "No web results found." 