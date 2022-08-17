import heapq

n = int(input())

q = []

for i in range(n):
    data = int(input())
    heapq.heappush(q, data)

result = 0

while len(q) != 1:
    one = heapq.heappop(q) # 알아서 늘 가장 작은 1개를 리턴해줌.
    two = heapq.heappop(q)
    sum_value = one + two
    result += sum_value
    print(result)

    heapq.heappush(q, sum_value)


print(result)



# 내가 처음 짠 코드는 가장 작은 걸 2개 더해서 리턴했다고 하더라도, 그게 가장 작다는 보장이 없음.

# N = int(input())
# array = []
#
# for _ in range(N):
#     array.append(int(input()))
#
# array.sort()
# length = len(array)
#
# if N == 1:
#     print(0)
#
# if N == 2:
#     print(array[0] + array[1])
#
# if N >= 3:
#
#     d = []
#     d.append(array[0])
#
#     for i in range(length - 1):
#         d.append(array[i+1] + d[i])
#
#
#     print(d)
#     print(sum(d[1:]))

# 반례 10, 20, 21, 22를 생각해보면 늘 가장 작은 2개를 뽑아내야됨을 알 수 있다.