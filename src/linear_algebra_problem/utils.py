import numpy as np

def linear_alg(arr):
    arr_np = np.array(arr)
    determinant = np.linalg.det(arr_np)
    return round(determinant, 2)