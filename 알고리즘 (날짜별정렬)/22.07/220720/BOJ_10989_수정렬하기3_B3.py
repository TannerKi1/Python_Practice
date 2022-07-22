import sys
N = int(input())

arr = [0] * 10001

# 0 , 1, 2, 3, 4, 5 ,...

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    arr[num-1] += 1


for i in range(1, 10001):
    while arr[i-1] > 0: #0부터 9999니까, 1부터 10000까지는 다 카운팅 될 수 있음!
        print(i)
        arr[i-1] -= 1


