from pymongo.mongo_client import MongoClient
from datetime import datetime
import os 
import ssl 

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
    
    '''
    for term,rates in prices.items():
        current_collection_name = collection_name(term)
        entry = {}
        entry['rates'] = rates 
        entry['time_inserted'] = datetime.now()
        database[current_collection_name].insert_one(entry) 
    #print('added')

def get_term_rates(term):
    '''
    Selects a specific rate from the database 
    '''
    pass 

def delete_rates():
    '''
    Deletes rates that are over a week old
    '''
