def sgd_to_term(sgd_rate, term_rate):
    """
    Converts term_rates relative to USD to SGD 

    1 USD = XX SGD
    1 UDS = YY ABC 
    
    XX SGD = YY ABC 
    1 SGD = YY/XX ABC 

    Parameters 
    ------------
    sgd_rate: SGD queried rates 
    term_rate: term queried rates 
    """

    return float(term_rate/sgd_rate)



