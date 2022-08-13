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

V, E = map(int, input().split())

parent = [0] * (V+1)

for i in range(1, V+1):
    parent[i] = i

array = []

for _ in range(E):
    a, b, cost = map(int, input().split())
    array.append((cost, a, b))

array.sort()


total = 0

for item in array:
    cost, a, b = item
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total += cost

print(total)

