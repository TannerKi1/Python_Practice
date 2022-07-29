import sys
N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
number_list = []
'''
for i in range(N):
    for j in range(1, N-i):
        if arr[i+j] > arr[i]:
            number_list.append(arr[i+j])
            break

    else:
        number_list.append(-1)

for x in number_list:
    print(x, end= ' ')
'''
# 시간 초과가 났음.
# for문을 2번 돌리지 않아도 되게..!

i = 0
while i < N:
    for j in range(1, N-i):
        if arr[i+j] > arr[i]:
            print(arr[i+j], end=' ')
            i += 1
            break

    else:
        i += 1
        print(-1, end=' ')

# while이나 for이나...


