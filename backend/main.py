from typing import Dict 
from threading import Thread
from flask import Flask, jsonify
from backend.mongodb.mongodb import rates_db, fetch_records
from backend.scheduler import periodic_query, periodic_delete, run_scheduler 
from backend.settings import QUERY_INTERVAL_MINUTES, DELETE_INTERVAL_MINUTES

app = Flask(__name__)

@app.route("/")
def ping():
    return ""

@app.route("/get/<base>/<time>")
def rate_interval(base: str, time: int) -> Dict:
    """
    Endpoint to fetch a specific base-term pair and time period
    
    Parameters:
        base: The base currency.
        time: The time period in days

    Returns:
        JSON response containing the fetched rates.
    """
    period = int(time)
    rates = fetch_records(rates_db, [base], period)

    return jsonify(rates) 

if __name__ == "__main__":
    scheduler_thread = Thread(target=run_scheduler)  # non-blocking of main app
    scheduler_thread.start()

    periodic_query(QUERY_INTERVAL_MINUTES)   
    periodic_delete(rates_db, DELETE_INTERVAL_MINUTES)  
    
    app.run(debug=True)