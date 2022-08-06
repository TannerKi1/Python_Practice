
array = list(map(int, input().split(',')))

b = [i for i in array if i % 2 != 0]

for k in b[:-1]:
    print(k, end = ', ')
print(b[-1])