N = int(input())
arr = []
for _ in range(N):
    name, score = input().split()
    arr.append((name, score))


arr = sorted(arr, key=lambda x: x[1]) # 람다 표현법

for student in arr:
    print(student[0], end=' ')







