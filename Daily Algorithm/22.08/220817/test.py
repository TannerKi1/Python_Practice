str1 = input()
str2 = input()

n = len(str1)
m = len(str2)

graph = [[0] * (m+1) for _ in range(n+1)]

for j in range(1, m+1):
    graph[0][j] = j

for i in range(1, n+1):
    graph[i][0] = i


for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1]:
            graph[i][j] = graph[i-1][j-1]
        else:
            graph[i][j] = min(graph[i-1][j-1], graph[i-1][j], graph[i][j-1]) + 1


print(graph[n][m])
