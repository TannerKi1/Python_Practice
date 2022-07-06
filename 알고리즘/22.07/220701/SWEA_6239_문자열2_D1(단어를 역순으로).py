

# 단어 단위를 역순으로 어떻게 구분할지?

# split 쓰면 될듯?


T_Map = list(map(str, input().split()))
k = T_Map[::-1]

for j in k:
    print(j, end = " ")