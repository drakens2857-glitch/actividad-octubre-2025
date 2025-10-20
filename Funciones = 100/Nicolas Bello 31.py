usuarios = ["Ana", "Luis", "Carlos"]
for i in range(10):
    print(f"Turno {i + 1}: {usuarios[i % len(usuarios)]}")
