'''def cycle_shift(A):
    A[:] = A[1:] + A[0:1]
'''

def cycle_shift(A): # сдвиг влево
    tmp = A[0]
    for i in range(len(A)-1):
        A[i] = A[i + 1]
    A[-1]= tmp

def cycle_shift(A): # сдвиг вправо
    tmp = A[-1]
    for i in range(len(A)-2, -1):
        A[i + 1] = A[i]
    A[0]= tmp
