def es_feliz(n):
    vistos = set()
    while n != 1 and n not in vistos:
        vistos.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1

for i in range(1, 101):
    if es_feliz(i):
        print(i)
