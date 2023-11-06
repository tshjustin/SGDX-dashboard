def get_sgd_rates(USD_base_rates): 
    '''
    Returns the rate of 1 SGD to 1 USD 
    '''
    oneUSD_to_oneSGD = USD_base_rates.get("SGD")
    oneSGD_to_oneUSD = float(1 / oneUSD_to_oneSGD)
    return oneSGD_to_oneUSD

def sgd_to_term(sgd_rate,term_rate): 
    '''
    Converts term currency from (1 USD -> Term) to (1 SGD -> Term)
    
    sgd_rate: 1 SGD -> 0.7XX USD (1 Unit of SGD) 
    
    1 SGD = 0.7XX USD
            1 USD = YY
    so, 1 SGD -> 0.7XX(YY)
    '''
    oneSGD_to_oneTerm = term_rate * sgd_rate
    return oneSGD_to_oneTerm

def term_to_sgd(sgd_rate,term_rate):
    '''
    Converts term currency from (1XXX -> 1 SGD) 
    '''
    
    pass
    
def converter(USD_base_rates):
    '''
    Converts all queried data from API from USDXXX to SGDXXX 
    
    USD_Base_rates: dictionary of key:value pairs 
    
    '''
    sgd_based_rates = {}
    sgd_usd_rate = get_sgd_rates(USD_base_rates)
    for term,rates in USD_base_rates.items():
        if term != 'SGD':
            sgd_based_rates[term] = sgd_to_term(sgd_usd_rate,rates)
    return sgd_based_rates
            
    

    
