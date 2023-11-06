from fastapi import FastAPI 
from query_price import fetch_rates
from utils import * 
from database_handler import * 
import asyncio
import datetime
import pytz

app = FastAPI() 

PREV_QUERY = 0

async def query_interval():
    '''
    Queries the Live API at 12pm SGD daily 
    '''
    global PREV_QUERY

    while True:
        now = datetime.datetime.now(pytz.timezone('Asia/Singapore'))

        # Determine the datetime for the next query at 12pm
        if now.hour < 12:
            next_query_time = now.replace(hour=12, minute=0, second=0, microsecond=0)
        else:
            # If current time is past 12pm, schedule the next query for 12pm the next day
            next_query_time = now + datetime.timedelta(days=1)
            next_query_time = next_query_time.replace(hour=12, minute=0, second=0, microsecond=0)
        
        # Calculate how many seconds to sleep until the next query time
        sleep_duration = (next_query_time - now).total_seconds()

        if sleep_duration <= 0:
            new_usd_rates = await fetch_rates()
            new_sgd_based_rates = converter(new_usd_rates)
            insert_rates(new_sgd_based_rates)
            delete_old_rates(new_sgd_based_rates)
            PREV_QUERY = int(now.timestamp())

            # Sleep for a short while before calculating the next 12pm
            await asyncio.sleep(60)  # Sleep for 1 minute - Incase it hammers the API again if the rates are not yet inserted 
        else:
            # Sleep until the next 12pm
            await asyncio.sleep(sleep_duration)

@app.on_event('startup')
def background_query():
    pass 
       
if __name__ == "_main__":
    uvicorn
    