from pymongo.mongo_client import MongoClient
from datetime import datetime, timedelta
from settings import MONGODB_KEY

class DatabaseHandler:
    
    def setup(self):
        client = MongoClient(MONGODB_KEY)
        self.database = client['SGDX']
        
    def collection_name(self, term):
        '''
        Generates the collection name for each currency type 
        '''
        return f'{term}_rates'

    def insert_rates(self, prices):
        '''
        Inserts rates from API call into the respective collections
        '''
        for term,rates in prices.items():
            current_collection_name = self.collection_name(term)
            entry = {}
            entry['rates'] = rates 
            entry['time_inserted'] = datetime.now()
            self.database[current_collection_name].insert_one(entry) 

    def get_term_rates(self, term):
        '''
        Gets the latest rate of a specific term 
        
        Since rates are queried at 12pm everyday, we would need to get the rates of the closest date 
        '''
        term_rates_name = self.collection_name(term)
        most_recent_record = next(self.database[term_rates_name].find().sort("time_inserted",-1).limit(1)) # Finds the latest record in a collection - next() is a pointer
        return most_recent_record['rates']
        
    def get_past_term_rates(self, duration, term):
        '''
        Gets a list of past rates (including current rates) for a specific current term rate
        
        rtype: list of past rates 
        ''' 
        term_rates_name = self.collection_name(term)
        cursor = self.database[term_rates_name].find().sort("time_inserted",-1).limit(duration)
        most_recent_records = list(cursor) # Note the cursor 
        return most_recent_records['rates']
        
    def delete_old_rates(self, prices):
        '''
        Deletes rates from the MongoDB that are 60 days old or older.
        '''
        # Calculate the date threshold: current date - 60 days
        threshold_date = datetime.now() - timedelta(days=60)
        for term in prices.keys():
            current_collection_name = self.collection_name(term)
            self.database[current_collection_name].delete_many({'time_inserted': {'$lt': threshold_date}})

dbm = DatabaseHandler()