def iter_power(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result
