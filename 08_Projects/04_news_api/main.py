from dotenv import load_dotenv
import requests
import os
from urllib.parse import quote_plus

load_dotenv()
news_api_key = os.getenv("NEWS_API_KEY")
if not news_api_key:
    raise RuntimeError("NEWS_API_KEY not found!")

query = "Artificial Intelligence"
params = {
    "q": query,
    # "from": "2025-07-19",
    "sortBy": "publishedAt",
    "apiKey": news_api_key,
}

encoded_query = quote_plus(query)
url = "https://newsapi.org/v2/everything"

print(f"Request URL: {requests.Request('GET', url, params=params).prepare().url}")

r = requests.get(url, params=params, timeout=10)
# print(r.json() if r.ok else r.text)
data = r.json()
articles = data['articles'] #it is a list of dictionaries

for index, articles in enumerate(articles):
    print(f"Article No: {index+1}")
    print(f"Title: {articles['title']}")
    print(f"Description: {articles['description']}")
    print(f"URL: {articles['url']}")
    print("*****************************************\n")

# r = requests.get(url)
