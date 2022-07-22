import sys
T = list(map(int, sys.stdin.readline().split()))
N = T[0]
X = T[1]

K = list(map(int, sys.stdin.readline().split()))
p = [j for j in K if j < X]
for x in p:
    print(x, end=' ')

# for문 2번만 돌려도 시간이 엄청 잡아먹히는 걸 확인할 수 있었다.