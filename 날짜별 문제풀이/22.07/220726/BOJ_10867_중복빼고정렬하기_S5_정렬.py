N = int(input())
arr = list(map(int, input().split()))

b = list(set(arr))
b.sort()

for x in b:
    print(x, end = ' ')

