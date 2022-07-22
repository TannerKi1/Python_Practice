
T = input()

a = []

for x in T:
    a.append(x)

m = 0
n = 0

for x_num in a:
    if x_num.islower():
        m += 1
    elif x_num.isupper():
        n += 1

print(f'UPPER CASE {n}')
print(f'LOWER CASE {m}')

