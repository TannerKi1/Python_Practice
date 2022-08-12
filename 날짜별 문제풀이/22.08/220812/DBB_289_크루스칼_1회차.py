def parent_check(parent, x):
    if parent[x] != x:
        parent[x] = parent_check(parent, parent[x])

    return parent[x]

def union(parent, a, b):
    a = parent_check(parent, a)
    b = parent_check(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())

parent = [0] * (V+1)
for i in range(1, V+1):
    parent[i] = i

edges = []
result = 0

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

# 비용이 저렴한 순으로 다리들의 후보가 담긴 상황.

for edge in edges:
    cost, start, end = edge
    if parent_check(parent, start) != parent_check(parent, end):
        result += cost
        union(parent, start, end)

print(result)

