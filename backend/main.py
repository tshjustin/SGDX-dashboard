import os 
import pytz
from typing import Dict, List
from threading import Thread
from datetime import datetime
from flask_cors import CORS 
from flask import Flask, jsonify
from backend.mongodb.mongodb import rates_db, fetch_records
from backend.scheduler import periodic_query, periodic_delete, run_scheduler, query_store
from backend.settings import QUERY_INTERVAL_MINUTES, DELETE_INTERVAL_MINUTES, logger, BASE_TERM_PAIRS

# Global variables for monitoring
scheduler_start_time = None
last_query_time = None
scheduler_thread = None

def create_app():
    app = Flask(__name__)

    # Allow CORS for all routes 
    CORS(app, resources={
        r"/*": { # match anypath of the defined backend endpoints 
            "origins": "*",  # all domain accepted 
            "methods": ["GET", "HEAD", "OPTIONS"], 
            "allow_headers": ["Content-Type"]
        }
    })
    
    if os.environ.get('GUNICORN_WORKER_ID', '0') == '0':
        initialize_scheduler()

    @app.route("/")
    def ping():
        logger.info("Ping endpoint hit")
        return "Service is running"

    @app.route("/get/<base>/<time>")
    def rate_interval(base: str, time: int) -> Dict:
        logger.info(f"Rate interval requested for {base} over {time} days")
        base = base.upper()
        period = int(time)
        rates = fetch_records(rates_db, [base], period)
        return jsonify(rates)

    @app.route("/get/terms")
    def terms() -> List:
        return BASE_TERM_PAIRS

    @app.route("/status")
    def status():
        global scheduler_thread, scheduler_start_time, last_query_time
        
        # Check DB status
        try:
            rates_db.command('ping')
            db_status = "connected"
        except Exception as e:
            db_status = f"error: {str(e)}"

        # Check rates API status
        import requests
        from backend.scraper.query_price import complete_url

        try:
            response = requests.head(complete_url)
            api_status = "accessible" if response.status_code == 200 else f"error: {response.status_code}"
        except Exception as e:
            api_status = f"error: {str(e)}"
        
        # Check scheduler status of worker 0 
        worker_id = os.environ.get('GUNICORN_WORKER_ID', 'unknown')

        if worker_id == '0':
            scheduler_status = scheduler_thread.is_alive() if scheduler_thread else False
            scheduler_start = scheduler_start_time.isoformat() if scheduler_start_time else None
            last_query = last_query_time.isoformat() if last_query_time else None
        else:
            # For non-scheduler workers, defer to worker 0's scheduler
            scheduler_status = "check worker 0"
            scheduler_start = "check worker 0"
            last_query = "check worker 0"

        # status payload 
        return jsonify({
            "service_status": "running",
            "scheduler_running": scheduler_status,
            "scheduler_start_time": scheduler_start,
            "last_query_time": last_query,
            "database_status": db_status,
            "api_status": api_status,
            "worker_id": worker_id
        })

    return app

def initialize_scheduler():
    global scheduler_thread, scheduler_start_time, last_query_time
    
    logger.info("Initializing scheduler")

    scheduler_start_time = datetime.now(pytz.utc)

    query_store()
    last_query_time = datetime.now(pytz.utc)
    logger.info("Initial query completed")
    
    periodic_query(QUERY_INTERVAL_MINUTES)
    periodic_delete(rates_db, DELETE_INTERVAL_MINUTES)

    scheduler_thread = Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
    logger.info("Scheduler thread started")
    
app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)