T = int(input())

for x in range(T):
    arr = [1] * 15000

    for i in range(2, 101):
        for j in range(i+i, 10001, i):
            arr[j] = 0

    even = int(input())
    half = even // 2

    for p in range(half, 1, -1):
        if arr[(even - p)] == 1 and arr[p] == 1:
            print(p, even-p)
            break


# 에라토스테네스의 체 최적화. while안쓰고 j를 i+i, 간격은 i로 두는 방법도 있다.
# 모든 경우를 리스트에 담아서 찾는 건 시간이 많이 걸림. 그냥 대입해서 조건에 맞으면 print하고 break하는 게 시간을 아낄 수 있다.










