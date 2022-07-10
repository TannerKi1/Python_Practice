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


# 자리수가 무지하게 많아지면, 문자열로 받아서 끝까지 돌린다음에 다 받아내면 됨!!
# 이후에 map 함수로 숫자열로 변환!






