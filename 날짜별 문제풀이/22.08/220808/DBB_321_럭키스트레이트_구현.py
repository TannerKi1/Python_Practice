k = input()
left = k[:len(k)//2]
right = k[len(k)//2:]

x, y = 0, 0

for i in left:
    x += int(i)

for i in right:
    y += int(i)

if x == y:
    print('LUCKY')

else:
    print('READY')
