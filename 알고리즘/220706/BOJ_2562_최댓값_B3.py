import sys

arr = []

for i in range(9):
    a = int(sys.stdin.readline().strip())
    arr.append(a)

print(max(arr))
print(arr.index(max(arr))+1)