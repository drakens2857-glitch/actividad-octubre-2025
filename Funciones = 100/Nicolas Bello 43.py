for i in range(16):
    print(hex(i)[2:].upper())
    for j in range(16):
        print(hex(i * 16 + j)[2:].upper(), end=' ')