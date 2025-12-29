import numpy as np

def Cohens(x_arr, y_arr, s_p):
    x_arr = x_arr
    y_arr = y_arr
    x_mean = np.mean(x_arr)
    y_mean = np.mean(y_arr)
    s_p = s_p

    numerator = abs(x_mean - y_mean)
    d = numerator / s_p

    return d