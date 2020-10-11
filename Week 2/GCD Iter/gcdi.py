def gcd_iter(a, b):
    """Returns the GCD of two positive integers."""
    smaller = a if a < b else b
    test_num = smaller
    while test_num > 1:
        if a % test_num == 0 and b % test_num == 0:
            return test_num
        test_num -= 1
        return 1
