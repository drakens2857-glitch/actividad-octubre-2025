texto = "murciélago"
texto = texto.lower().replace(" ", "")
es_isograma = True
for letra in texto:
    if texto.count(letra) > 1:
        es_isograma = False
        break
print(es_isograma)
