import numpy as np

def OneSampT(x_mu, y_mu, x_arr, y_arr):
    x_arr = x_arr
    y_arr = y_arr

    x_mean = np.mean(x_arr)
    y_mean = np.mean(y_arr)

    x_mu = x_mu
    y_mu = y_mu

    x_std = np.std(x_arr, ddof=1)
    y_std = np.std(y_arr, ddof=1)
    
    n_x     = len(x_arr)
    n_y     = len(y_arr)

    x_numerator = x_mean - x_mu
    y_numerator = y_mean - y_mu

    x_denominator = x_std / np.sqrt(n_x)
    y_denominator = y_std / np.sqrt(n_y)

    x_t = x_numerator / x_denominator
    y_t = y_numerator / y_denominator

    return x_t, y_t