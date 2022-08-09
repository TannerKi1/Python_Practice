n = int(input()) #집의 개수

arr = list(map(int, input().split()))

distance = []
for house in arr:
    cnt = 0
    for j in range(n):
        cnt += abs(house - arr[j])
    distance.append((house, cnt))

distance.sort(key = lambda x: (x[1], x[0]))

print(distance)
print(distance[0][0])

# 상당히 원시적인 방법
# 수학적으로 생각하면, 모든 집들의 위치를 받은 뒤 해당 집들의 가장 중간값을 리턴해주면 된다.
#
# arr.sort()
#
# print(arr[(len(arr) - 1) // 2])

# 값이 홀수이면 무조건 중앙, 값이 짝수이면 왼쪽에 있는 것. 위의 식으로 돌려보면 어떻게든 같은 값이 2개 나오게 된다.