import math

min, max = map(int, input().split())

max_sqrt = int(math.sqrt(max))

number_bool_list = [True] * (max_sqrt + 1)

for number in range(2, max_sqrt + 1):
    j = 2
    while number * j <= max_sqrt:
        number_bool_list[number * j] = False
        j += 1

prime = []
idx = 2
for p in number_bool_list[2:]:
    if p:
        prime.append(idx**2)
    idx += 1

'''
prime = []

for x in range(2, int(math.sqrt(max))+1):
    prime.append(x**2)
'''

num = max - min + 1

arr_2 = [0] * num

for y in prime:
    j = math.ceil(min/y)
    while y * j <= max:
        tmp = y * j - min
        if arr_2[tmp] == 0:
            arr_2[tmp] = 1
            num = num - 1
        # 좀 멋있었다.
        j += 1

print(num)
