import time
import schedule
from backend.mongodb.mongodb import *
from backend.scraper.query_price import fetch_rates
from backend.conversion.convert_rates import convert_rates_to_sgd_base

def periodic_delete(rates_db: MongoClient, interval: int) -> None:
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
    global last_query_time
    try:
        prices = fetch_rates()
        sgd_base_prices = convert_rates_to_sgd_base(prices)
        insert_records(rates_db, sgd_base_prices)
        last_query_time = datetime.now(pytz.utc)
        logger.info("Query executed successfully")
        
    except Exception as e:
        logger.error(f"Query failed: {str(e)}", exc_info=True)
        raise