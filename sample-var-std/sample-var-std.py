import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    arr = np.array(x)
    mean_val = np.mean(arr)
    sum = 0
    for i in range (arr.shape[0]):
        sum += (arr[i] - mean_val) ** 2
    variance_val = (1/(arr.shape[0] - 1))*sum
    sd_val = np.sqrt(variance_val)
    return (variance_val, sd_val)
    pass