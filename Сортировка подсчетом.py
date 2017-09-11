Q = [0]*10
N = int(input())
for i in range(N):
    x = int(input())
    Q[x] += 1
for digit in range(10):
    for i in range(Q[digit]):
        print(digit, end = " ")
