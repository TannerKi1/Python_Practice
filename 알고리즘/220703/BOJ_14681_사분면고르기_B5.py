T = 2
tray = []

for _ in range(1, T+1):
    b = int(input())
    tray.append(b)

X = tray[0]
Y = tray[1]

if X > 0 and Y > 0:
    print(1)

if X < 0 and Y > 0:
    print(2)

if X < 0 and Y < 0:
    print(3)

if X > 0 and Y < 0:
    print(4)




