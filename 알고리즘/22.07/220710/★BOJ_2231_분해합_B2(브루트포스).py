N = int(input())

answer = []

for k in range(1, N):
    arr = []

    for j in str(k):
        arr.append(j)

    arr_int = map(int, arr)

    if sum(arr_int) + int(k) == N:
        answer.append(k)

if len(answer) >= 1:
    print(min(answer))

else:
    print(0)









