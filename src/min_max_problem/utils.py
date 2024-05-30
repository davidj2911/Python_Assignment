import numpy as np

def min_max():
    n, m = [int(num) for num in input().split(' ')]

    arr = []
    for _ in range(n):
        arr.append([int(num) for num in input().split(' ')])

    return (np.max(np.min(arr, axis=1)))
