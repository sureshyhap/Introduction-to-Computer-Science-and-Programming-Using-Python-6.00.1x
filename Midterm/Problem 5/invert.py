def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    inverse = {}
    for key, value in d.items():
        if value not in inverse.keys():
            l = [key]
            inverse[value] = l
        else:
            inverse[value].append(key)
            inverse[value].sort()
    return inverse
