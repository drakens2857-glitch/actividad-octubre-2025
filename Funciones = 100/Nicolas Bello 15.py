def es_primo(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

n = 100
for i in range(2, n):
    if es_primo(i) and es_primo(i + 2):
        print((i, i + 2))
