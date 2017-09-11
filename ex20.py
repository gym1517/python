def pseudo_list():
    for i in range(N):
        yield (i*9876 + 1024)%1000

N = 10**6 + 1
#N = 15

B = []
A = pseudo_list()
Q = [0]*1000
sum = 0

for i in A:
    Q[i] += 1
    sum += i

for digit in range(1000):
    for i in range(Q[digit]):
        B.append(digit)

print(B[:])

print(Q[:])
print(N//2 + 1)
print(B[N//2])
print(B[N//2-2:N//2+3])
print(sum)

# Другой метод как в экзамене

x = 0
sum_count = Q[0]
while sum_count <= N//2:
    x += 1
    sum_count += Q[x]
print(x)
