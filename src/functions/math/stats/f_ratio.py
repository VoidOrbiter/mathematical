def FRatio(groups_list, ssw, ssb):
    k = len(groups_list)

    total_n = sum(len(group) for group in groups_list)

    dfb = k - 1
    dfw = total_n - k

    msb = ssb / dfb
    msw = ssw / dfw
    
    f = msb / msw

    eta_sq = ssb / (ssb + ssw)

    return f, eta_sq