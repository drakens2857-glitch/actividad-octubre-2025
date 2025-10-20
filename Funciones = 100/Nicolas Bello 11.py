from string import ascii_lowercase
texto = "El veloz murciélago hindú comía feliz cardillo y kiwi"
texto = texto.lower()
es_pangrama = all(letra in texto for letra in ascii_lowercase)
print(es_pangrama)
