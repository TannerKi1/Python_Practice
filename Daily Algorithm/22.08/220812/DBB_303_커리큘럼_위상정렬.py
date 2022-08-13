import copy
from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)] # 각 번호들의 연결 그래프를 담을 곳

# 진입차수 잡아주기
indegree = [0] * (N+1)

time = [0] * (N+1)

for i in range(1, N+1):
    data = list(map(int, input().split())) # -1로 범위값으로 받아야해서
    time[i] = data[0] #data로 들어온 것 중에 맨 앞에 있는게 현재 강의의 시간값

    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)


    for i in range(1, N+1):
        print(result[i])

topology_sort()




