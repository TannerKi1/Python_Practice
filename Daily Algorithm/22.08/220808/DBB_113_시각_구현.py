# 3중 포문 구현

N = int(input())
cnt = 0

for i in range(0, N+1):
    for j in range(0, 60):
        for k in range(0, 60): # 60초가 0이니까... 60은 들어가면 안 됨
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)