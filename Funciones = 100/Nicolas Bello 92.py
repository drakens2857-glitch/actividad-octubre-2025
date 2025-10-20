def multiplos_de_siete(n):
    for i in range(1, n + 1):
        yield i * 7

for m in multiplos_de_siete(10):
    print(m, end=" ")
