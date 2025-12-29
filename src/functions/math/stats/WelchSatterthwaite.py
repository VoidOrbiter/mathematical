import numpy as np

def WelchSW(x_arr, y_arr):
    x_arr   = x_arr
    y_arr   = y_arr
    x_mean  = np.mean(x_arr)
    y_mean  = np.mean(y_arr)
    x_s     = np.var(x_arr, ddof=1)
    y_s     = np.var(y_arr, ddof=1)
    x_n     = len(x_arr)
    y_n     = len(y_arr)

    numerator = ((x_s / x_n) + (y_s / y_n))**2
    denominator = (((x_s / x_n)**2 / (x_n - 1)) + (y_s / y_n)**2 / (y_n - 1))

    df = numerator / denominator

    return df