N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

first = arr[-1]
second = arr[-2]

set_num = M // (K+1)
margin_num = M % (K+1)

answer = (first * K + second * 1) * set_num + (margin_num * first)

print(answer)


# 묶음 단위로 생각하면 편하다.