import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y_arr = np.asarray(y)
    clean = y_arr[y_arr >= 0]
    if len(clean) == 0:
        return 0.0 
    classes, counts = np.unique(clean, return_counts=True)
    prob = counts / len(clean)
    entropy = -np.sum(prob * np.log2(prob + 1e-15))
    return np.maximum(0.0, entropy)
    
    pass