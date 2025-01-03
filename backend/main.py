from flask import Flask
from threading import Thread
from backend.scheduler import periodic_query, periodic_delete, run_scheduler 
from backend.settings import QUERY_INTERVAL_MINUTES, DELETE_INTERVAL_MINUTES

app = Flask(__name__)

@app.route("/")
def ping():
    return ""

@app.route("/get/<time>")
def rate_interval(time):
    return time 

if __name__ == "__main__":
    scheduler_thread = Thread(target=run_scheduler)  # non-blocking of main app
    scheduler_thread.start()

    periodic_query(QUERY_INTERVAL_MINUTES)   
    periodic_delete(DELETE_INTERVAL_MINUTES)  
    
    app.run(debug=True)