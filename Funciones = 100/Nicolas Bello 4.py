texto = "Python es un lenguaje poderoso y versátil"
contador = 0
for palabra in texto.split():
    if len(palabra) > 5:
        contador += 1
print(contador)
