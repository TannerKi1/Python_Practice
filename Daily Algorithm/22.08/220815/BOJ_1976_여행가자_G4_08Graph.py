N = int(input())
M = int(input())


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


array = []
for _ in range(N):
    array.append(list(map(int, input().split())))


visited = list(map(int, input().split()))

parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i


group_list = []

for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            group_list.append((i+1, j+1))

visited_list = []

for i in range(M-1):
    visited_list.append((visited[i], visited[i + 1]))


for item in group_list:
    x, y = item
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)


for item in visited_list:
    x, y = item
    if find_parent(parent, x) != find_parent(parent, y):
        print("NO")
        exit()
print("YES")
