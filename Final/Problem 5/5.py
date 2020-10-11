def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = {}
    difference = {}
    for key1, value1 in d1.items():
        if key1 in d2.keys():
            intersect[key1] = f(value1, d2[key1])
        else:
            difference[key1] = value1
    for key2, value2 in d2.items():
        if key2 not in d1.keys():
            difference[key2] = value2
    return (intersect, difference)

def f(a, b):
    return a > b

d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}

print(dict_interdiff(d1, d2))
