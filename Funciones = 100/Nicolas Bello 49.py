numero = 123456789
suma = 0
for d in str(numero):
    if int(d) % 2 == 0:
        suma += int(d)
print(suma)
