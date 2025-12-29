import numpy as np

def PooledStd(x_arr, y_arr):
    x_arr = x_arr
    y_arr = y_arr
    x_s   = np.var(x_arr, ddof=1)
    y_s   = np.var(y_arr, ddof=1)
    x_n   = len(x_arr)
    y_n   = len(y_arr)

    numerator =((x_n -1) * x_s) + ((y_n - 1) * y_s)
    denominator = x_n + y_n - 2

    sp = np.sqrt(numerator / denominator)

    return sp