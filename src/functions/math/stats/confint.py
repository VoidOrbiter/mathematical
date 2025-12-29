import numpy as np
from scipy.stats import norm, t

def ConfInt(z_val, x_arr, y_arr):
    x_arr   = x_arr
    y_arr   = y_arr
    z_val   = z_val

    z_float = float(z_val)

    z_frac  = z_float / 100
    x_mean  = np.mean(x_arr)
    y_mean  = np.mean(y_arr)

    x_std   = np.std(x_arr, ddof=0)
    y_std   = np.std(y_arr, ddof=0)

    s_x     = np.std(x_arr, ddof=1)
    s_y     = np.std(y_arr, ddof=1)

    n_x     = len(x_arr)
    n_y     = len(y_arr)
    
    x_std_err   = s_x / np.sqrt(n_x)
    y_std_err   = s_y / np.sqrt(n_y)

    alpha       = 1 - z_frac
    two_tail    = alpha / 2

    z_star      = norm.ppf(1 - two_tail)
    x_t_star    = t.ppf(1 - two_tail, df=n_x-1)
    y_t_star    = t.ppf(1 - two_tail, df=n_y-1)

    ci_lower_x  = x_mean - x_t_star * x_std_err
    ci_upper_x  = x_mean + x_t_star * x_std_err

    ci_lower_y  = y_mean - y_t_star * y_std_err
    ci_upper_y  = y_mean + y_t_star * y_std_err
    
    
    return ci_lower_x, ci_upper_x, ci_lower_y, ci_upper_y