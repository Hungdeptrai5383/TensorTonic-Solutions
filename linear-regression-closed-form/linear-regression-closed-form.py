import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    x_trans = np.transpose(X, (1,0))
    N = x_trans @ X
    N_invert = np.linalg.inv(N)
    return N_invert @ x_trans @ y
    pass