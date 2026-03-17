import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    if not (0 <= p <= 1):
        raise ValueError("Probability p must be between 0 and 1.")
    if k < 0 or k > n:
        return 0.0, 0.0 # Probability is zero if k is out of bounds

    # PMF for the specific k
    pmf = comb(n, k) * (p**k) * ((1 - p)**(n - k))
    
    # CDF: Sum of PMFs from 0 to k (inclusive)
    cdf = 0
    for i in range(k + 1):
        cdf += comb(n, i) * (p**i) * ((1 - p)**(n - i))
        
    return (pmf, cdf)
    pass