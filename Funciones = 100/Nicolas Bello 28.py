letras = "ABCDEFGHIJ"
for i in range(len(letras)):
    if i % 2 == 0:
        print(letras[i])
    else:
        print(' ' * i + letras[i])
