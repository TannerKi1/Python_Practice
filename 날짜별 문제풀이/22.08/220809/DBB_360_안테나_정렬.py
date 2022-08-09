n = int(input()) #집의 개수

arr = list(map(int, input().split()))

distance = []
for house in arr:
    cnt = 0
    for j in range(n):
        cnt += abs(house - arr[j])
    distance.append((house, cnt))

distance.sort(key = lambda x: (x[1], x[0]))

print(distance[0][0])