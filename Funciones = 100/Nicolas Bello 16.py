import random
A = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
B = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
C = [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]
print(C)
for row in C:
    print(row)