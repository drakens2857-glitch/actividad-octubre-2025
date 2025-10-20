letras = "ABCDEFGHIJ"
for i in range(len(letras)):
    print(letras[i] if i % 2 == 0 else letras[i].lower())
