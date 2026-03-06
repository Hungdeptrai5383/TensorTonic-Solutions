import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    arr = np.array(X)
    if arr.ndim != 2 or arr.shape[0] < 2:
        return None
    meanvec = np.mean(arr, axis = 0)
    xcent = arr - meanvec
    ans = (xcent.T @ xcent) / (arr.shape[0] - 1)
    return ans

    pass