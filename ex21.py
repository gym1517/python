str = "Sam is a multi-file text editor based on structural regular expressions It was originally designed in the early 1980s at Bell Labs by Rob Pike with the help of Ken Thompson and other Unix developers for the Blit windowing terminal running on Unix it was later ported to other systems Sam follows a classical modular Unix aesthetic It is internally simple its power leveraged by the composability of a small command language and extensibility through shell integration"

A = sorted(str.split(" "))
print(A)
n = len(A)
print(n)

print(A[n//2])

B = str.split()
print(B)
for pos in range(n - 1):
    for i in range(pos + 1, n):
        if B[i] < B[pos]:
            B[i], B[pos] = B[pos], B[i]
print(B)
print(B[n//2])




