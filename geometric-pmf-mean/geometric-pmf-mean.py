import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    arr = np.array(k)
    pmf = np.zeros((arr.shape))
    if not (0 <= p <= 1): 
        return None
    for i in range (arr.shape[0]):
        pmf[i] = pow(1-p, arr[i]-1)*p
    return (pmf, 1/p)
    pass