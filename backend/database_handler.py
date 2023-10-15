from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv, find_dotenv
import os 

load_dotenv(find_dotenv)

client = MongoClient(os.environ.get('MONGO_URL_KEY'))
database = client['SGDX']

#Each collection would hold a currency-pair: Name of each collection is term_rates

def collection_name(term):
    '''
    Generates the collection name for each currency type 
    '''
    return f'{term}_rates'

def insert_rates(prices):
    '''
    Inserts rates from API call into the respective collections
    
    #Needs to include current Datetime, but will be done in main! 
    '''
    for term,rates in prices.items():
        current_collection_name = collection_name(term)
        database[current_collection_name].insertOne(rates)
