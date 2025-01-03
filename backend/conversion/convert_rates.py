from typing import Dict 
from backend.scraper.query_price import fetch_rates

def sgd_to_term(sgd_rate: float, term_rate: float) -> float:
    """
    Converted rate = SGD_rate / Term_rate 

    Parameters: 
        sgd_rate: SGD queried rates 
        term_rate: term queried rates 
    
    Returns :
        term_rate in terms of SGD base 
    """

    return float(term_rate / sgd_rate)

def convert_rates_to_sgd_base(prices: Dict) -> Dict: 
    """
    Converts all base_term pairs to SGD as base 

    SGD_rate = Term_rate / USD_to_SGD_rate 

    Parameters:     
        prices: Dictionary of all USD_base: term pairs 

    Returns: 
        prices: Dictionary of all SGD_base: term pairs 
    
    """ 
    updated_prices = {}
    usd_sgd_rate = prices["SGD"]
    for term, term_rate in prices.items(): 
        updated_prices[term] = sgd_to_term(usd_sgd_rate, term_rate) # inverse as shown 

    prices.update(updated_prices)

    # Converts SGD->USD => USD->SGD 
    prices["USD"] = float(1 / usd_sgd_rate)
    prices.pop("SGD")

    return prices 

if __name__ == "__main__":
    prices = fetch_rates()
    print(convert_rates_to_sgd_base(prices))