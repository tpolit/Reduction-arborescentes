def decomposition(n):
    if n == 0:
        return [False]
    elif n == 1:
        return [True]
    else:
        return [(n % 2 == 1)] + decomposition(n//2)


def completion(tab_bin, n):
    while len(tab_bin) < n:
        tab_bin += [False]
    return tab_bin[:n]


def table(x, n):
    return completion(decomposition(x), n)