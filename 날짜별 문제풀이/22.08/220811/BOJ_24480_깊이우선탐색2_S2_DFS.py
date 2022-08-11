import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E, start = map(int, input().split())

graph = [[] for _ in range(V + 1)]

visited = [False] * (V + 1)

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, V+1):
    graph[i].sort(reverse=True)

cnt = 1  # 전역변수 설정하기.
answer = [0] * (V + 1)

def dfs(start):

    global cnt
    visited[start] = True
    answer[start] = cnt

    for i in graph[start]:
        if not visited[i]:
            cnt += 1
            dfs(i)

dfs(start)

for i in range(1, V + 1):
    print(answer[i])


