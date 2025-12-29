import numpy as np

def Covariance(x_arr, y_arr):
    x_dev_list      = []
    y_dev_list      = []
    product_list    = []
    
    x_mean = np.mean(x_arr)
    y_mean = np.mean(y_arr)
    for i in range(len(x_arr)):
        x_dev   = x_arr[i] - x_mean
        y_dev   = y_arr[i] - y_mean
        product = x_dev * y_dev

        x_dev_list.append(x_dev)
        y_dev_list.append(y_dev)
        product_list.append(product)

    covariance = sum(product_list) / len(x_arr)

    return x_dev_list, y_dev_list, product_list, covariance