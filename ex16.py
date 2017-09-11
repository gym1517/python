my_list = [(lambda x:(x*87+12)%16) (i) for i in range(20)]

print(my_list)
m = 100
k = 0
while len(my_list) != 0:
    x = my_list.pop()
    if m > x:
        m = x
        k = 1
        print(">   ", m, x)
    elif m == x:
        k += 1
        print("=   ",m, x)
    print ("    ", m, x)
print(my_list)
print(k)
