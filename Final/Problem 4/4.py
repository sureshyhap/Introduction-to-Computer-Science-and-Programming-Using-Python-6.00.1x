def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    L.sort(reverse=True)
    length = len(L)
    i = 0
    while True:
        count = 0
        num = L[i]
        while L[i] == num:
            count += 1
            i += 1
            if i == length:
                break
        if count % 2 == 1:
            return num
        elif count % 2 == 0 and i == length:
            return None
