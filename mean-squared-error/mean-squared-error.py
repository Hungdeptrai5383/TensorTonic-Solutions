import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    pred = np.array(y_pred)
    true = np.array(y_true)
    ans = 0
    if pred.shape != true.shape:
        return None
    for i in range (pred.shape[0]):
        ans += (pred[i] - true[i])**2
    return ans/pred.shape[0]
    pass
