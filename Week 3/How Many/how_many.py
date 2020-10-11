def how_many(aDict):
    """Returns how many values are in a dictionary of lists."""
    count = 0
    for vals in aDict.values():
        count += len(vals)
    return count

        
print(how_many(animals))
