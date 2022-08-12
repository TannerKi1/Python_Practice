N, M = map(int, input().split())

parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i # 집합노드


edges = [] # 모든 도로들의 정보가 들어가있음.
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

### 사전 준비 완료

### 함수 준비 시작


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

total = 0


for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        total += cost
        ### 마지막 cost
        last = cost



