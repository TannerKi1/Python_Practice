
N = 333456
c = [0] * 10

for _ in range(6):
    k = N % 10
    c[k] += 1
    N = N // 10

tri = 0
run = 0


for i in range(0, 9):
    if c[i] == 3:
        tri += 1
        c[i] -= 3

for j in range(0, 7):
    if c[j] and c[j+1] and c[j+2] >= 1:
        c[j] -= 1
        c[j+1] -= 1
        c[j+2] -= 1
        run += 1

if tri + run == 2:
    print("Found Answer")