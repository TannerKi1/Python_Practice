array = [[1], [1, 1]]

n = int(input())

for i in range(2, n):
    k = list()
    k.append(1)
    for j in range(1, i):
        k.append(array[i - 1][j - 1] + array[i - 1][j])
    k.append(1)
    array.append(k)

print(array)