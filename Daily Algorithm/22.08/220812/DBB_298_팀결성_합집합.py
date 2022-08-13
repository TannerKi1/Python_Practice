V, E = map(int, input().split())

parent = [0] * (V+1)

for i in range(1, V+1):
    parent[i] = i


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


for _ in range(E):
    order, a, b = map(int, input().split())
    if order == 0:
        union_parent(parent, a, b)
    elif order == 1:
        if find_parent(parent, a) != find_parent(parent, b):
            print("NO")
        else:
            print("YES")

