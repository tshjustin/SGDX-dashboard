import time 
import schedule 
from flask import Flask 
from scraper.query_price import fetch_rates
from conversion.convert_rates import sgd_to_term

app = Flask(__name__) 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# flask --app main run
def query_store() -> None:
    prices = fetch_rates()

    # COnvert to sgd base 

    # store data 

def periodic_query(interval: int) -> None: 
    """
    Queries the endpoint after {time} interval 

    Arguments: 
        interval: Time interval in minutes for each query 
    """
    schedule.every(interval).minutes.do(fetch_rates)

def run_scheduler() -> None:
    """
    Continuously run the scheduler and checks for executed jobs 
    """
    while True:
        schedule.run_pending()
        time.sleep(1)