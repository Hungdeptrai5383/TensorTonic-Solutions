import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    if len(x) == 0:
        return None, None, None
    arr = np.array(x)
    mean_val = np.mean(arr)
    median_val = np.median(arr)
    counts = Counter(arr)
    mode_val = counts.most_common(1)[0][0]
    return mean_val, median_val, mode_val
    pass