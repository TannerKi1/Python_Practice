N, M = map(int, input().split())
S = dict()
for _ in range(N):
    S[input()] = True

# 딕셔너리로 해야 시간 이득이 더 나올 것 같긴함.
# set_S를 딕셔너리로 바꿔서 저장해보자.

count = 0
for _ in range(M):
    if input() in S.keys():
        count += 1

print(S)
print(count)


# 이게 되네;