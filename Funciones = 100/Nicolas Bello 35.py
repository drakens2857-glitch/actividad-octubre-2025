letras = "ABCDEFGHI"
for i in range(1, len(letras) + 1, 2):
    print(letras[:i].center(len(letras)))
for i in range(len(letras) - 2, -1, -2):
    print(letras[:i].center(len(letras)))