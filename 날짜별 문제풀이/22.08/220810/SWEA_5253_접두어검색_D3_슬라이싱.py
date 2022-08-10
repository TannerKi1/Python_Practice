import time
T = int(input())

start = time.time()
for tc in range(1, T+1):
    A, B = map(int, input().split())
    arr1 = []
    for _ in range(A):
        arr1.append(input())

    cnt = 0

    for _ in range(B):
        k = input()
        x = len(k)

        for item in arr1:
            if item[0:x] == k:
                cnt += 1
                break

    print(f'#{tc} {cnt}')

print(time.time() - start)


