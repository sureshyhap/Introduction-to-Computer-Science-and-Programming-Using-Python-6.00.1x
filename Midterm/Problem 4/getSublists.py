def getSublists(L, n):
    """ L is a list of integers, n is an integer.
    Returns a list of subLists of contiguous elements
    in L of length n each."""
    subLists = []
    i = 0
    length = len(L)
    while n + i <= length:
        subLists.append(L[i:n+i])
        i += 1
    return subLists
