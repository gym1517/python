# Циклический сдвиг влево
'''def cycle_shift(A):
    A[:] = A[1:] + A[0:1]
'''

def cycle_shiftl(A): # сдвиг влево
    tmp = A[0]
    for i in range(len(A)-1):
        A[i] = A[i + 1]
    A[-1]= tmp

def cycle_shiftr(A): # сдвиг вправо
    tmp = A[-1]
    for i in range(len(A)-2, -1, -1):
        A[i + 1] = A[i]
    A[0]= tmp

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(A)

cycle_shiftl(A)
print(A)

cycle_shiftr(A)
print(A)
