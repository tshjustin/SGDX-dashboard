import os 
import requests #Allows sending of HTTP requests to URL 
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from utils import get_sgd_rates, sgd_to_term

URL = 'https://api.currencyapi.com/v3/latest'

BASE_TERM_PAIRS = ["BND","CNY","HKD","IDR","INR",
            "JPY","KRW","LKR","MYR", "PHP", 
            "SGD","THB","VND"]

params = { #params vs headers 
    'apikey' : os.environ.get('CURRENCY_API_KEY')
}

def fetch_rates():
    '''
    Fetches the current rates from API in the form of USDXXX 
    
    :return: JSON of rates 
    :rtype: Dictionary - With key:value pairs of base:value
    '''
    response = requests.get(URL, params=params)
    data = response.json()
    
    prices = {} #CountryCode:value
    for term, term_rate in data['data'].items(): 
        if term in BASE_TERM_PAIRS:
            prices[term] = term_rate['value']
    return prices

if __name__ == '__main__':
    prices = fetch_rates()
    sgd_rate = get_sgd_rates(prices)
    term = sgd_to_term(sgd_rate,30)
    print(term)