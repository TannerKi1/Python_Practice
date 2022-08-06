N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

print(graph) # 따로 split을 하지 않아도 개별 얼음틀처럼 들어가는 것을 확인할 수 있음.