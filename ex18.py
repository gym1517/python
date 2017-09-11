from math import sqrt

my_list = [(lambda x:(x*87+12)%100)(i) for i in range(20)]

print(my_list)
s = s2 = 0
n = len(my_list)

while len(my_list):
    x = my_list.pop()
    s += x
    s2 += x**2

print(round(sqrt(s2/n - (s/n)**2),5))
print(my_list)

