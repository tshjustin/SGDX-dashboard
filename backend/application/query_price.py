import requests 
from utils import * 
from settings import API_URL, API_KEY

BASE_TERM_PAIRS = ["BND","CNY","HKD","IDR",
                   "INR","JPY","KRW","LKR",
                   "MYR", "PHP", "SGD","THB",
                   "VND"]

params = {
    'apikey' : API_KEY
}

def fetch_rates():
    '''
    Fetches the current rates from API in the form of USDXXX 
    
    :return: JSON of rates 
    :rtype: Dictionary - With key:value pairs of base:value
    '''
    response = requests.get(API_URL, params=params)
    data = response.json()
    
    prices = {} # CountryCode: value
    for term, term_rate in data['data'].items(): 
        if term in BASE_TERM_PAIRS:
            prices[term] = term_rate['value']
    return prices


if __name__ == "__main__":
    a = fetch_rates()