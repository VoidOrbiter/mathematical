import numpy as np

def SpearmanRanks(arr):
    sorted_pairs = sorted(enumerate(arr), key=lambda x: x[1])
    ranks = [0] * len(arr)
    i = 0
    while i < len(arr):
        j = i
        while j + 1 < len(arr) and sorted_pairs[j+1][1] == sorted_pairs[i][1]:
            j += 1
        avg_rank = (i + 1 + j + 1) / 2
        for k in range(i, j + 1):
            idx = sorted_pairs[k][0]
            ranks[idx] = avg_rank
        i = j + 1
    return ranks

def SpearmanCoeff(arr1, arr2):
    x_ranks = SpearmanRanks(arr1)
    y_ranks = SpearmanRanks(arr2)

    x_mean_rank = np.mean(x_ranks)
    y_mean_rank = np.mean(y_ranks)

    x_dev = [x - x_mean_rank for x in x_ranks]
    y_dev = [y - y_mean_rank for y in y_ranks]

    cov_rank = sum(x_dev[i] * y_dev[i] for i in range(len(x_dev))) / len(x_dev)

    x_std = np.sqrt(sum(d**2 for d in x_dev) / len(x_dev))
    y_std = np.sqrt(sum(d**2 for d in y_dev) / len(x_dev))

    rho = cov_rank / (x_std * y_std)
    return rho