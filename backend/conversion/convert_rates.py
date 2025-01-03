def sgd_to_term(sgd_rate: float, term_rate: float) -> float:
    """
    Converts term_rates relative to USD to SGD 

    1 USD = XX SGD
    1 UDS = YY ABC 
    
    XX SGD = YY ABC 
    1 SGD = YY/XX ABC 

    Parameters: 
        sgd_rate: SGD queried rates 
        term_rate: term queried rates 
    
    Returns :
        sgd_term: term_rate
    """

    return float(term_rate/sgd_rate)



