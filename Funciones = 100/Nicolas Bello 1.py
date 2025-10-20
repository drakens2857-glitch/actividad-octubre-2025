cadena = "aabbccdde"
repetido = False
for i in range(1, len(cadena)):
    if cadena[i] == cadena[i - 1]:
        repetido = True
        break
print(repetido)
