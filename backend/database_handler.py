from pymongo.mongo_client import MongoClient
from datetime import datetime
import os 

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

def get_term_rates(term):
    '''
    Gets the latest rate of a specific term 
    
    Since rates are queried at 12pm everyday, we would need to get the rates of the closest date 
    '''
    term_rates_name = collection_name(term)
    most_recent_record = next(database[term_rates_name].find().sort("time_inserted",-1).limit(1)) #finds the latest record in a collection - next() is a pointer
    return most_recent_record['rates']
    
def get_past_term_rates(duration,term):
    '''
    Gets a list of past rates (including current rates) for a specific current term rate
    
    rtype: list of past rates 
    ''' 
    term_rates_name = collection_name(term)
    cursor = database[term_rates_name].find().sort("time_inserted",-1).limit(duration)
    most_recent_records = list(cursor) #Note the cursor 
    return most_recent_records['rates']
    

def delete_rates():
    '''
    Deletes rates that are over a week old
    '''
    pass 
