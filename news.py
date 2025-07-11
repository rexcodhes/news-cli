import pprint
from newsapi import NewsApiClient
import requests
from db import top_headlines
from db import all_articles
from db import breaking_headlines_db
API_KEY = 'f0ae88245ae84088a22a037c66e9f2f2'

newsapi = NewsApiClient(API_KEY)

def get_top_headlines():
        
        c1 = input("Enter the title of the news article: ")
        c2 = input("Enter the category of the news article: ")
        c3 = input("Enter the language of the news article: ")
        c4 = input("Enter the country of the news article: ")
        url = ('https://newsapi.org/v2/top-headlines')

        params = {
        "q": c1,
        "category": c2,
        "language": c3,
        "country": c4,
        "apiKey": API_KEY
    }
        # Make the request to the News API
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
        
            for i, article in enumerate(data.get("articles", []), 1):
             print(f"{i}. {article['title']} ({article['source']['name']})")
             print(article['url'])
             print()
             top_headlines.insert_one(article)
       
        else:
         print("Failed to fetch news:", response.status_code, response.text)
   
   
def get_everything():
        c1 = input("Enter the title of the news article: ")
        c2 = input("Enter sorting criteria (relevancy, popularity, publishedAt): ")
        c3 = input("Enter the language of the news article: ")
        url = ('https://newsapi.org/v2/everything')

        params = {
        "q": c1,
        "sortBy": c2,
        "language": c3,
        "pageSize": 10,
        
        "apiKey": API_KEY
    }
        # Make the request to the News API
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
        
            for i, article in enumerate(data.get("articles", []), 1):
             print(f"{i}. {article['title']} ({article['source']['name']})")
             print(article['url'])
             print()
             all_articles.insert_one(article)
       
        else:
         print("Failed to fetch news:", response.status_code, response.text)

def breaking_headlines():
     c1 = input("Enter the name of the country (e.g., us, gb, in): ")
     
     url = "https://newsapi.org/v2/top-headlines"
     params = {
        "country": c1,
        "apiKey": API_KEY
    }

     response = requests.get(url, params=params)

     if response.status_code == 200:
        data = response.json()
        for i, article in enumerate(data.get("articles", []), 1):
            print(f"{i}. {article['title']} ({article['source']['name']})")
            print(article['url'])
            print()
            breaking_headlines_db.insert_one(article)
     else:
        print("Failed to fetch news:", response.status_code, response.text)
    
sources = newsapi.get_sources()





