# 이건 버블 정렬이 되나?
# N개 정도니까?

N = int(input())
arr = []

for i in range(N):
    K = int(input())
    arr.append(K)


for k in range(len(arr)-1):
    for j in range(len(arr)-1-k):
        if arr[j] >= arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1]

for p in arr:
    print(p)