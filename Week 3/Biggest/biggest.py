def biggest(aDict):
    """Returns the key corresponding to the entry with the largest
    number of values associated with it."""
    max_length = 0
    key_corresponding = None
    for key, value in aDict.items():
        if len(value) > max_length:
            key_corresponding = key
            max_length = len(value)
    return key_corresponding


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))
