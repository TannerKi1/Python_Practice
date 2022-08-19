import sys
input = sys.stdin.readline

n = input()
T = int(input())

for _ in range(T):
    a, b, c = input().split()
    ib = int(b)
    ic = int(c)

    cnt = 0
    array = [0]
    for i in range(len(n)):
        if n[i] == a:
            cnt += 1
        array.append(cnt)



    print(array[ic+1] - array[ib])


