N, M = map(int, input().split())

arr = list(map(int, input().split()))

max_temp = -99999
for i in range(N-M+1):
    if sum(arr[i:i+M]) >= max_temp:
        max_temp = sum(arr[i:i+M])

print(max_temp)
