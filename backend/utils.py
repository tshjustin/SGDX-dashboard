def get_sgd_rates(rates): 
    '''
    Returns the rate of 1 SGD to 1 USD 
    '''
    oneUSD_to_oneSGD = rates.get("SGD")
    oneSGD_to_oneUSD = float(1 / oneUSD_to_oneSGD)
    return oneSGD_to_oneUSD

def sgd_to_term(sgd_rate,term_rate): 
    '''
    Converts all currency from (1 USD -> Term) to (1 SGD -> Term)
    
    sgd_rate: 1 SGD -> 0.732 USD (1 Unit of SGD) 
    
    1 SGD = 0.7XX USD
            1 USD = YY
    so, 1 SGD -> 0.7XX(YY)
    '''
    oneSGD_to_oneTerm = term_rate * sgd_rate
    return oneSGD_to_oneTerm
    
    
def term_to_sgd(sgd_rate,term_rate):
    '''
    Converts all currency from 1 Term to 1 SGD 
    '''
    pass
    
    
