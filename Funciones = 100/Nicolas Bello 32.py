def triangulares(n):
    for i in range(1, n + 1):
        yield i * (i + 1) // 2

for t in triangulares(10):
    print(t, end=" ")
