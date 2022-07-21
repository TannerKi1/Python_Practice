# 화폐단위를 섞어서 특정 금액 만들어보기

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input())) #2원이랑 3원이 array에 들어가게 됨

d = [10001] * (m+1) # 알고 싶은 금액의 가장 끝


d[0] = 0
for i in range(n):
    for j in range(array[i], m+1): # 코인 종류와, 끝까지 가야하는 총액으로 나뉨
        if d[j - array[i]] != 10001: # 2원을 만드는 방법이 존재한다면,
            d[j] = min(d[j], d[j - array[i]] + 1)


if d[m] == 10001:
    print(-1)

else:
    print(d[m])


# BOJ_2839_설탕배달로 연결됨