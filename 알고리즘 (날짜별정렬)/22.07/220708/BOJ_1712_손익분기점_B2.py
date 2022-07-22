arr = list(map(int, input().split()))
A = arr[0]
B = arr[1]
C = arr[2]
answer = 1
while (A + (B * answer)) / answer >= C:
    answer += 1
else:
    print(answer)
