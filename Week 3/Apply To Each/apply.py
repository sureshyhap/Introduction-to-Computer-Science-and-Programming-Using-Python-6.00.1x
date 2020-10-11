testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

# applyToEach(testList, abs)

def add1(num):
    return num + 1

# applyToEach(testList, add1)

def square(num):
    return num ** 2

applyToEach(testList, square)


