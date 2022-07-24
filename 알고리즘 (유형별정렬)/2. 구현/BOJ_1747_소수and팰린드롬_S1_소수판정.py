
arr = [0] * 2000000

for i in range(2, 1440):
    for j in range(i+i, 2000000, i):
        arr[j] = 1


n = int(input())

if n == 1:
    print(2)
    exit()

if n >= 2:
    for z in range(n, 2000000):
        if arr[z] == 0:
            if str(z) == str(z)[::-1]:
                print(z)
                break



