texto = "El águila vuela alto sobre el océano"
vocales = "aeiouáéíóú"
contador = 0
for palabra in texto.lower().split():
    if palabra[0] in vocales:
        contador += 1
print(contador)
