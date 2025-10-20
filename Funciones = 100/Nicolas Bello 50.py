votos = ["A", "B", "A", "C", "B", "A", "C", "C", "B"]
conteo = {}
for voto in votos:
    conteo[voto] = conteo.get(voto, 0) + 1
print(conteo)
