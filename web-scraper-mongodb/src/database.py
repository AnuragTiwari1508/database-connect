from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URI"))
        self.db = self.client[os.getenv("DB_NAME")]
        self.collection = self.db["scrape_results"]

    def insert_scrape_result(self, url, content):
        result = {
            "url": url,
            "content": content
        }
        self.collection.insert_one(result)

    def get_all_scrape_results(self):
        return list(self.collection.find())