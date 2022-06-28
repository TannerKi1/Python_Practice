

a = [1, 3, 6, 78, 35, 55]
b = [12, 24, 35, 24, 88, 120, 155]

c = []
for i in a:
    for j in b:
        if j == i:
            c.append(j)

print(c)