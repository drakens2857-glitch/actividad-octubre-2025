letras = "ABCDE"
n = len(letras)
for i in range(n):
    print(' ' * (n - i - 1) + letras[:i + 1])
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + letras[:i + 1])
