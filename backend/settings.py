from dotenv import load_dotenv, find_dotenv
import os 
import logging

load_dotenv(find_dotenv())

# Logger 
logging.basicConfig(level=logging.WARNING) 

# Database 
MONGO_CONNECTION = os.environ.get('MONGO_CONNECTION')

# External APIs 
API_URL = os.environ.get('API_URL')

API_KEY = os.environ.get('CURRENCY_API_KEY')

# Constants 
QUERY_INTERVAL_MINUTES = 10 
DELETE_INTERVAL_MINUTES = 1440 

BASE_TERM_PAIRS = ["BND","CNY","HKD","IDR",
                   "INR","JPY","KRW","LKR",
                   "MYR", "PHP", "SGD","THB",
                   "VND"]