def number(random_seed):
    return(random_seed*693 + 5)%100

"""
for i in range(20):
    n = number(i)
    print(i, n, number(i))
"""
sum = 0
s = 0
i = 1
while number(i) != 0:
    if number(i)%4 == 0:
        s += 1
        sum += number(i)
        print(number(i))
    i += 1
    print(number(i), i)
print(s, sum, sum//s)
print([number(i) for i in range(1,20)])

