a, b = map(int, input().split())

a_yak = []
b_yak = []

for i in range(1, a+1):
    if a % i == 0:
        a_yak.append(i)

for i in range(1, a+1):
    if b % i == 0:
        b_yak.append(i)

common_yak = []

for k in a_yak:
    if k in b_yak:
        common_yak.append(k)

GDB = max(common_yak)

a_2 = a / GDB
b_2 = b / GDB

print(GDB)
print(int(a_2 * b_2 * GDB))