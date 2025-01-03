import time
import schedule
from backend.scraper.query_price import fetch_rates
from backend.mongodb.mongodb import delete_records, insert_records
from backend.conversion.convert_rates import convert_rates_to_sgd_base

def periodic_delete(interval: int = 1440) -> None:
    """
    Schedules the deletion of old records at the specified time interval.
    
    Arguments:
        interval: Time interval in minutes for each deletion task.
    """
    schedule.every(interval).minutes.do(delete_records)

def periodic_query(interval: int) -> None:
    """
    Queries the endpoint after {time} interval.
    
    Arguments:
        interval: Time interval in minutes for each query.
    """
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
    insert_records(sgd_base_prices)