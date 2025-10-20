def factoriales(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f

for f in factoriales(10):
    print(f, end=" ")
