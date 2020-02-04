def gcdRecur(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
