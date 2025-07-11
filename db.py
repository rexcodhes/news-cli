import os
import pymongo
import pathlib
from dotenv import load_dotenv



env_path = pathlib.Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

client = pymongo.MongoClient(os.environ["MONGODB_URI"])

db = client['news']
top_headlines = db['top_headlines']
all_articles = db['all_articles']
breaking_headlines_db = db['breaking_headlines']
