import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    arr = np.array(x)
    pro = np.array(p)
    if arr.shape != pro.shape:
        raise ValueError
    if np.sum(pro) != 1:
        raise ValueError
    ans = 0
    for i in range (arr.shape[0]):
        ans += arr[i]*pro[i]
    return ans
    pass
