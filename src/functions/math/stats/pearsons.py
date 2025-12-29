import numpy as np

def Pearson(x_dev_list, y_dev_list, covariance):

    x_sq = [x**2 for x in x_dev_list]
    y_sq = [y**2 for y in y_dev_list]

    x_var = sum(x_sq) / len(x_sq)
    y_var = sum(y_sq) / len(y_sq)

    x_std = np.sqrt(x_var)
    y_std = np.sqrt(y_var)

    std_prod = x_std * y_std
    r = covariance / std_prod

    return r