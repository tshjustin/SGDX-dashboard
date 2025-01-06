import pytz
from typing import Dict, List 
from datetime import datetime, timedelta
from pymongo import MongoClient, ASCENDING
from backend.settings import MONGO_CONNECTION, BASE_TERM_PAIRS

mongo_client = MongoClient(MONGO_CONNECTION)
rates_db = mongo_client.get_database("SGDX_Rates")

def create_schema(rates_db: MongoClient, currencies: List[str]) -> None:
    """
    Creates the tables of foreign pairs if collection does not exist 

    Parameters: 
        rates_db: MongoDB instance 
        currencies: List of currencies to store 
    """ 
    for currency in currencies: 
        collection = rates_db[currency] 
        collection.create_index([("timestamp", ASCENDING)], unique=True)

def insert_records(rates_db: MongoClient, prices: Dict[str, float]) -> None:
    """
    Insert SGD_base: Term_rates into the relevant currency collections

    Schema: { rates: float, timestamp: datetime}
    
    Parameters:
        rates_db: MongoDB database instance
        prices: Dictionary of prices in terms of SGD Base
    """
    utc_time = datetime.now(pytz.utc)
    
    for currency, rate in prices.items():
        record = {
            "rate": rate,
            "timestamp": utc_time 
        }
        rates_db[currency].insert_one(record)

def delete_records(rates_db: MongoClient, days: int = 60) -> None:
    """
    Delete records that are older than the specified number of days and minutes.
    
    Parameters:
        rates_db: MongoDB database instance.
        days: Number of days to retain records.
    """
    cutoff_time = datetime.now(pytz.utc) - timedelta(days=days)  # Get the UTC time cutoff

    for collection_name in rates_db.list_collection_names():
        rates_db[collection_name].delete_many({"timestamp": {"$lt": cutoff_time}})

def fetch_records(rates_db: MongoClient, currency: List[str], period: int) -> Dict[str, Dict[str, float]]:
    """
    Fetches records for the last `period` days.
    """
    cutoff_datetime = datetime.now(pytz.utc) - timedelta(days=period)
    
    currencies = {}
    for curr in currency:

        records = rates_db[curr].find({"timestamp": {"$gte": cutoff_datetime}})
        currencies[curr] = {
            str(record["timestamp"]): record["rate"] for record in records
        }
    
    return currencies

create_schema(rates_db, BASE_TERM_PAIRS)

# Returns a payload of the form: 
# {
#     "USD": {
#         "20250101": 1.35,
#         "20250102": 1.36,
#         "20250103": 1.37,
#         ...
#     },
#     "MYR": {
#         "20250101": 1.15,
#         "20250102": 1.16,
#         "20250103": 1.17,
#         ...
#     }
# }