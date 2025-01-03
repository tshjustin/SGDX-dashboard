from typing import Dict, List 
from pymongo import MongoClient
from backend.settings import MONGO_CONNECTION

"""
Database: SGDX_Rates, where each table is a Foreign Currency 

Schema of Foregin Rate: 
        _id: ObjectID String 
        rate: float 
        timestamp : YYYYMMDD 
"""

def connect_to_mongo() -> None:
    client = MongoClient(MONGO_CONNECTION)
    rates_db = client.get_database("SGDX_Rates")
    return rates_db

def create_schema() -> None:
    """
    Creates the tables of foreign pairs
    """ 

def insert_records(prices: Dict) -> None: 
    """
    Insert SGD_base: Term_rates into the table 
    
    Parameters: 
        prices: Dictionary of prices in terms of SGD Base 
    """

def delete_records() -> None: 
    """
    Delete records that are older than 60 Days 
    """

def fetch_records(currency: List[str], period: int) -> Dict[str, Dict[str, float]]: 
    """
    Fetches records based on: 
    1. Type of currency wanted 
    2. Requested Time Period 
    
    Parameters: 
        currency: List of strings of wanted currency
        period: how to diff between minutes / days / months ? 

    Return: 
        currencies: Dictionary of currency: {time: rates}
    """