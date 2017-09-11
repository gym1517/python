def inverse(A):
    A[:] = A[::-1]

B = [1,2,3,4,5]
inverse(B)
print(*B)
