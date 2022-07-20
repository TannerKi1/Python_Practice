# 부분집합 구하는 문제.


N, S = map(int, input().split())
arr = list(map(int, input().split()))

i = len(arr)

arr_2 = [0] * (1<<i)
arr_3 = []

for i in range(1<<i):
    mini = []
    for j in range(len(arr)):
        if i & (1<<j) == 0:
            mini.append(arr[j])
    arr_3.append(mini)

count = 0
for x in arr_3:
    if len(x) !=0:
        if sum(x) == S:
            count += 1

print(count)
