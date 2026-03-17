import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    arr = np.array(x)
    if p > 1 or p < 0:
        raise ValueError
    pmf = np.zeros((arr.shape[0]))
    for i in range (arr.shape[0]):
        if arr[i] == 0:
            pmf[i] = 1 - p
        else:
            pmf[i] = p
    return (pmf, p, p*(1-p))
    pass