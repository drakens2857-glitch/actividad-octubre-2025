def cuadrados(n):
    for i in range(1, n + 1):
        yield i**2

for c in cuadrados(10):
    print(c, end=" ")
