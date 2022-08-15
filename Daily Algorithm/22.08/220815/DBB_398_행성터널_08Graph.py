

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

N = int(input())
parent = [0] * (N+1)


for i in range(1, N+1):
    parent[i] = i


x = []
y = []
z = []

for i in range(1, N+1):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

edges = []

x.sort()
y.sort()
z.sort()

result = 0

for i in range(N - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))


edges.sort()


for edge in edges:
    cost, x, y = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost


print(result)


