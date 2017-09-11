my_list = [(lambda x:(x*296+2410)%4096) (i) for i in range(2000)]

min1 = min2 = my_list.pop()
k = 0
while len(my_list):
    x = my_list.pop()
    if x <= min1:
        min1 = x
    elif x < min2:
        min2 = x
        k = 1
    elif x == min2:
        k += 1

print(my_list)
print(k, min1, min2)
