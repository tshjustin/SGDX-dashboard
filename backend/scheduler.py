import time
import schedule
from backend.mongodb.mongodb import *
from backend.scraper.query_price import fetch_rates
from backend.settings import MONGO_CONNECTION, BASE_TERM_PAIRS
from backend.conversion.convert_rates import convert_rates_to_sgd_base

mongo_client = MongoClient(MONGO_CONNECTION)
rates_db = mongo_client.get_database("SGDX_Rates")
create_schema(rates_db, BASE_TERM_PAIRS)

def periodic_delete(rates_db, interval: int = 1440) -> None:
    schedule.every(interval).minutes.do(lambda: delete_records(rates_db)) # for the sake of argument passing 

def periodic_query(interval: int) -> None:
    schedule.every(interval).minutes.do(query_store)

def run_scheduler() -> None:
    while True:
        schedule.run_pending()
        time.sleep(1)

def query_store() -> None:
    """
    Query, convert and store 
    """
    prices = fetch_rates()
    sgd_base_prices = convert_rates_to_sgd_base(prices)
    insert_records(rates_db, sgd_base_prices) # else we can do as such to pass the arugments in 