import numpy as np

def SSWithin(groups_list):
    ssw = 0
    for group in groups_list:
        mean_i = np.mean(group)
        ssw += np.sum((group - mean_i)**2)
    return ssw