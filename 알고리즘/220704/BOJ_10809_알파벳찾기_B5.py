S = str(input())
k = [-1] * 26
p = 'abcdefghijklmnopqrstuvwxyz'
for i in range(0, 26):
    k[i] = S.find(p[i])
    print(k[i], end=' ')
