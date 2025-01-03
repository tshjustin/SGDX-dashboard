import logging 
import requests 
from typing import Dict 
from backend.settings import API_URL, API_KEY, BASE_TERM_PAIRS # python -m scraper.query_price resolves relative imports. Run module name, not module path (with .py)

complete_url = f"{API_URL}?api_key={API_KEY}"

def fetch_rates() -> Dict:
    """
    Queries API for base:term pairs 

    Returns:
        dict: Dictionary of term-base pairs 

    """
    response = requests.get(complete_url)
    data = response.json()
    
    prices = {} # CountryCode: value
    for term, term_rate in data['rates'].items():
        if term in BASE_TERM_PAIRS:
            prices[term] = term_rate

    logging.info("Query Successful")
    return prices

# prices = {"SGD": 1.34, "MYR": 3.22, ...}
