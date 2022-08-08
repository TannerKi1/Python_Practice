x = input()

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
char = []
cnt = 0
for k in x:
    if k not in num:
        char.append(k)
    else:
        cnt += int(k)

char.sort()

b = ''
for x in char:
    b += x

print(b, end = '')
print(cnt)
