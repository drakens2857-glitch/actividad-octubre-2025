def primos_hasta(n):
    for x in range(2, n + 1):
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                break
        else:
            yield x

for p in primos_hasta(50):
    print(p, end=" ")
