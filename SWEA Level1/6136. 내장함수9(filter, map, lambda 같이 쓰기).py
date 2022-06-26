
a = [x for x in range(1,11)]

b = []

for even_number in filter(lambda x: x % 2 == 0, a):
    b.append(even_number)

c = list(map(lambda x: x**2, b))

print(c)