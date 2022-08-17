N = int(input())
arr = list(map(int, input().split()))

arr.sort()

start = 0
end = len(arr)

mid = (start + end - 1) // 2

print(arr[mid])