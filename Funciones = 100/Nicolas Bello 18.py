lista = [1, 2, 3, 2, 1]
es_palindromo = True
for i in range(len(lista) // 2):
    if lista[i] != lista[-(i + 1)]:
        es_palindromo = False
        break
print(es_palindromo)
