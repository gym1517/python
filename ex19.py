from math import sqrt

my_list = [(lambda x:(x*87+12)%100)(i) for i in range(20)]

print(my_list)
s = s2 = 0
n = 0

while len(my_list) >0:
    x = my_list.pop()
    if x%2 == 0:
        n += 1
        s += x
        s2 += x**2

print(round(sqrt(s2/n - (s/n)**2),2))
print(my_list)

