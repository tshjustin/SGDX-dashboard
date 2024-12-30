def get_sgd_rates(USD_base_rates): 
    '''
    Rates from API based in USD. SGD Rates inferred from its USD base. 
    
    Returns 1 sgd: base usd 
    '''
    oneUSD_to_SGD = USD_base_rates.get("SGD")
    return float(1 / oneUSD_to_SGD)
     
def sgd_to_term(sgd_rate,term_rate): 
    '''
    Converts term currency from (1 USD -> Term) to (1 SGD -> Term)
    
    sgd_rate: 1 SGD -> 0.7XX USD (1 Unit of SGD) 
    
    1 SGD = 0.7XX USD
            1 USD = YY
    '''
    oneSGD_to_oneTerm = term_rate * sgd_rate
    return oneSGD_to_oneTerm

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

