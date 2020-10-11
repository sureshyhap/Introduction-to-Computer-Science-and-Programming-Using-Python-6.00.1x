# test_tup = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    """Captures every other element in a tuple and records it in another tuple.
    """
    result_tup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            result_tup += (aTup[i],)
    return result_tup

print(oddTuples(test_tup))
