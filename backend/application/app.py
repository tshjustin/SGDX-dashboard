from flask import Flask, jsonify
import schedule
import threading
import logging
import time
from query_price import fetch_rates
from database_handler import dbm
from utils import converter  
from settings import QUERY_INTERVAL_HOUR

app = Flask(__name__)

logger = logging.getLogger(__name__)

def run_continuously(interval=6*60*60): 
    '''
    interval: sets default time in seconds to check and run pending task 
    '''
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

def periodic_query():
    '''
    Queries external API, Converts to SGD base and storage.
    '''
    usd_rates = fetch_rates()
    sg_rates = converter(usd_rates)
    dbm.insert_rates(sg_rates)
    logger.info("Rates successfully stored!")

def initialize_cron():
    '''
    Initializes CronJob 
    '''
    schedule.every(QUERY_INTERVAL_HOUR).hours.do(periodic_query)  
    stop_run_continuously = run_continuously()
    logger.info("Cron initialized!")

def init_app():
    '''
    Initializes Database & cron 
    '''
    dbm.setup()
    initialize_cron()
    return app

@app.route('/')
def ping():
    return 'Root - For pinging purposes'

@app.route('/rates/<term>')
def term_base(term):
    rates = dbm.get_term_rates(term)
    print(f'SGD to {term} Rates:', rates) 
    return jsonify({term: rates})

if __name__ == "__main__":
    app = init_app()
    app.run(host='0.0.0.0', debug=False)