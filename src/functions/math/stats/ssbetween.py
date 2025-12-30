import numpy as np

def SSBetween(groups_list, grand_mean):
    ssb = 0
    for group in groups_list:
        n_i = len(group)
        mean_i = np.mean(group)
        ssb += n_i * (mean_i - grand_mean)**2
    return ssb