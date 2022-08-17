N = int(input())
array = list(map(int, input().split()))
target = int(input())

array_set = set(array)

cnt = 0
for i in array:
    k = target - i
    if k in array_set and array.index(i) < array.index(k):
        cnt += 1
    else:
        continue

print(cnt)

