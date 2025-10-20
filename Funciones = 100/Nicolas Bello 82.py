def impares_hasta(n):
    for i in range(1, n + 1, 2):
        yield i

for i in impares_hasta(20):
    print(i, end=" ")
