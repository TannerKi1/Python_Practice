import sys
N, M = map(int, input().split())

dex = []

for x in range(N):
    dex.append(sys.stdin.readline().strip())

dict = {dex[x]: x+1 for x in range(len(dex))} # 여기서 x가 이미 int 값으로 바뀌어서 value로 들어갔고...
dict_2 = {v:k for k, v in dict.items()}

for y in range(M):
    t = sys.stdin.readline().strip() # 여기서 주어지는 t는 str값이니까
    if t[0].isupper():
        print(dict[t])

    elif t[-1].isupper():
        print(dict[t])

    else:
        print(dict_2[int(t)]) # 다시 부르기 위해서는 int t로 바꿔야함.







