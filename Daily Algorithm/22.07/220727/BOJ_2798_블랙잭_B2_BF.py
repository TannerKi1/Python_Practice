N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if arr[i]+arr[j]+arr[k] == M:
                print(M)
                exit()
            elif arr[i]+arr[j]+arr[k] < M:
                answer.append(arr[i]+arr[j]+arr[k])


print(max(answer))








