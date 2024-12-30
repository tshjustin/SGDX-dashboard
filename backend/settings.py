from dotenv import load_dotenv, find_dotenv
import os 
import logging

load_dotenv(find_dotenv())

# Logger 
logging.basicConfig(level=logging.DEBUG) 

# Database 
MONGODB_KEY = os.environ.get('MONGO_URL_KEY')

# External APIs 
API_URL = os.environ.get('API_URL')

API_KEY = os.environ.get('CURRENCY_API_KEY')

# Constants 
QUERY_INTERVAL_HOUR = 6 

QUERY_INTERVAL_SECONDS = 10 