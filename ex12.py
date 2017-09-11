def generate_number():
    return lambda random_seed: (random_seed*693 + 5)%100

number = generate_number()
s = 0
i = 0
while number(i) != 0:
    if number(i)%7 == 0:
        s += 1
    i += 1
    print(number(i), i)
print(s)
print([number(i) for i in range(1,20)])
