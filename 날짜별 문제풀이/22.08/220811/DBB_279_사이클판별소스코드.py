
def cycle_check(parent, x):
    if parent[x] != x:
        parent[x] = cycle_check(parent, parent[x])

    return parent[x]


def cycle_union(parent, a, b):
    a = cycle_check(parent, a)
    b = cycle_check(parent, b)

    if a < b :
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())  # 노드 3개 간선 3개

parent = [0] * (v + 1)


Cycle = False

for i in range(1, v + 1):
    parent[i] = i

cnt = 0
for _ in range(e):
    a, b = map(int, input().split())
    if cycle_check(parent, a) == cycle_check(parent, b):
        Cycle = True
        cnt += 1
        break

    else:
        cycle_union(parent, a, b)
        cnt += 1

if Cycle:
    print("사이클이 발생했습니다.")
    print(cnt)

else:
    print("순환이 없는 그래프입니다.")
    print(cnt)





