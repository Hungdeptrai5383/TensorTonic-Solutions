def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    arr = np.array(X)
    num_samples, num_features = arr.shape
    x_trans = np.transpose(arr, (1,0))
    I = np.eye(num_features)
    inner = x_trans @ arr + lam * I
    invert_inner = np.linalg.inv(inner)
    return invert_inner @ x_trans @ y