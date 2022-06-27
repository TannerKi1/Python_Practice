
a = [12, 24, 35, 70, 88, 120, 155]

b = []

# a[1], a[3], a[5] 만 프린트 하면 됨

for k in a:
    b = []
    for k in range (1,6):
        if k % 2 != 0:
            b.append(a[k])

print(b)



