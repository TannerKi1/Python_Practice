S = str(input())

k = [-1] * 26
p = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(0, 26):
    k[i] = S.find(p[i])

for j in k:
    print(j, end = ' ')