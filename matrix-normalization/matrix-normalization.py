import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    mat = np.array(matrix, dtype=float)
    if axis is not None and axis >= mat.ndim:
        return None
    if mat.ndim != 2:
        return None
    if norm_type == 'l1':
        norm = np.sum(np.abs(mat), axis=axis, keepdims=(axis is not None))
    elif norm_type == 'l2':
        norm = np.sqrt(np.sum(mat**2, axis=axis, keepdims=(axis is not None)))
    elif norm_type == 'max':
        norm = np.max(np.abs(mat), axis=axis, keepdims=(axis is not None))
    else:
        return None
    norm = np.where(norm == 0, 1, norm)
        
    return mat / norm