def genPrimes():
    yield 2
    n = 2
    while True:
        n += 1
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
