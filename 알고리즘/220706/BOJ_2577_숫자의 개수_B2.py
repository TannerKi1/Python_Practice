
k = []

for _ in range(3):
    number = int(input())
    k.append(number)

num_2 = k[0]*k[1]*k[2]

s_num_2 = str(num_2)

dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

for char in s_num_2:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

for (key, val) in dict.items():
    print(val)





