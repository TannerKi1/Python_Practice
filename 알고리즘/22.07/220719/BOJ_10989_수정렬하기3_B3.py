N = int(input())
empty_array = []
for x in range(N):
    empty_array.append(int(input()))

empty_array.sort()

for x in empty_array:
    print(x)

