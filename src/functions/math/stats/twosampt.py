import numpy as np

def TwoSampT(x_arr, y_arr):
    x_arr = x_arr
    y_arr = y_arr
    x_mean = np.mean(x_arr)
    y_mean = np.mean(y_arr)

    x_var = np.var(x_arr, ddof=1)
    y_var = np.var(y_arr, ddof=1)

    x_n = len(x_arr)
    y_n = len(y_arr)

    numerator = x_mean - y_mean
    denominator = np.sqrt((x_var / x_n) + (y_var / y_n))

    t_neg = numerator / denominator
    t = abs(t_neg)

    return t