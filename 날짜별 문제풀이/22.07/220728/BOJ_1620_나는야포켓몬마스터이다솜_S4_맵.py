import sys
N, M = map(int, input().split())

dex = []

for x in range(N):
    dex.append(sys.stdin.readline().strip())

dict = {dex[x]: x+1 for x in range(len(dex))} # 여기서 x가 이미 int 값으로 바뀌어서 value로 들어갔고...
dict_2 = {v:k for k, v in dict.items()} # key랑 value를 바꿔서 저장하는 법은 반드시 알아놓도록.

for y in range(M):
    t = sys.stdin.readline().strip() # 여기서 주어지는 t는 str값이니까
    if t[0].isupper():
        print(dict[t])

    elif t[-1].isupper():
        print(dict[t])

    else:
        print(dict_2[int(t)]) # 다시 부르기 위해서는 int t로 바꿔야함.





# map을 이용해서 O(1)의 속도로 불러오는 게 포인트. 자바 강의 듣다가 생각나서 기록 남김 (220809)

