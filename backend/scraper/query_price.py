import logging 
import requests 
from typing import Dict 
from backend.settings import API_URL, API_KEY, BASE_TERM_PAIRS # python -m scraper.query_price resolves relative imports. Run module name, not module path (with .py)

complete_url = f"{API_URL}?api_key={API_KEY}"

logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__)

def fetch_rates() -> Dict:
    """
    Queries API for base:term pairs 

    Returns:
        dict: Dictionary of term-base pairs 
    """
    try:
        response = requests.get(complete_url)
        response.raise_for_status() 
        
        data = response.json()
        prices = {}  # CountryCode: value
        
        for term, term_rate in data['rates'].items():
            if term in BASE_TERM_PAIRS:
                prices[term] = term_rate
        
        logger.info("Query successful")
        return prices
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Query failed, {e}")
        return {}

# prices = {"SGD": 1.34, "MYR": 3.22, ...}
