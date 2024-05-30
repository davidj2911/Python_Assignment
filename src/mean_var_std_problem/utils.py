import numpy as np

def mean_var_std(array):
    mean = np.mean(array, axis=1)
    var = np.var(array, axis=0)
    std = round(np.std(array, axis=None), 3)
    result = f"{mean}\n{var}\n{std}"
    return result