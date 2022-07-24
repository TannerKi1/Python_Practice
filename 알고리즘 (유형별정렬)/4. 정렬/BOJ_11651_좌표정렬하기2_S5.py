T = int(input())
arr = []
for x in range(T):
    n, m = map(int, input().split())
    arr.append((n, m))

arr.sort(key = lambda x: x[0])
arr.sort(key = lambda x: x[1])

for a, b in arr:
    print(a, b)
