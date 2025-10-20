def pares_hasta(n):
    for i in range(2, n + 1, 2):
        yield i

for p in pares_hasta(20):
    print(p, end=" ")
