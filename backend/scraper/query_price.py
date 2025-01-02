import requests 
from backend.settings import API_URL, API_KEY

BASE_TERM_PAIRS = ["BND","CNY","HKD","IDR",
                   "INR","JPY","KRW","LKR",
                   "MYR", "PHP", "SGD","THB",
                   "VND"]

complete_url = f"{API_URL}?api_key={API_KEY}"

def fetch_rates():
    '''
    Fetches the current rates from API in the form of USDXXX 
    
    :return: JSON of rates 
    :rtype: Dictionary - With key:value pairs of base:value
    '''
    response = requests.get(complete_url)
    data = response.json()
    
    prices = {} # CountryCode: value
    for term, term_rate in data['rates'].items():
        if term in BASE_TERM_PAIRS:
            prices[term] = term_rate
    return prices

def periodic_query(time): 
    '''
    Queries Endpoint every period 
    
    '''


if __name__ == "__main__":
    print(fetch_rates())