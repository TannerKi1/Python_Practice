N = int(input())
arr = []
for _ in range(N):
    arr.append(input().split())


arr.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

print(arr)


# sort를 순서대로 정렬하는 방법 우선순위를 주는 방법이다.





