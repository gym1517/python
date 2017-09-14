A = [2, 4, 4, 4, 6, 6, 7, 10]

def left_bound(A, x):
    """ индекс позиции MAX числа из списка, которое меньше x
        :param A: массив чисел
        :param x: # x - искомое число в массиве
    :return:
    """
    left = -1   # вначале наша позиция - перед списком
    right = len(A)  - 1 #все числа с этой позиции правее X

    while left + 1 < right:
        middle = (left + right)//2
        if A[middle] <= x:
            left = middle
        else:
            right = middle

    while A[left] == x:
        left -= 1

    return left + 1

print(left_bound(A, 2))
print(left_bound(A, 4))
print(left_bound(A, 6))
print(left_bound(A, 10))
print(left_bound(A, 12))
