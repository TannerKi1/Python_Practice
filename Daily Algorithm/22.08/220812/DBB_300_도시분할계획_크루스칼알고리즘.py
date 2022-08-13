V, E = map(int, input().split())

parent = [0] * (V+1)

for i in range(1, V+1):
    parent[i] = i

road = []

for _ in range(E):
    data = map(int, input().split())
    a, b, cost = data
    road.append((cost, a, b))

road.sort()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

real_road = list()

for item in road:
    cost, a, b = item
    if find_parent(parent, a) != find_parent(parent, b):
        real_road.append(cost)
        union_parent(parent, a, b)

print(sum(real_road) - real_road[-1])

