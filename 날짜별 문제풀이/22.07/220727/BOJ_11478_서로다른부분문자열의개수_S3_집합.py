S = input()

arr = []
for i in range(len(S)):
    for j in range(i, len(S)+1):
        arr.append(S[i:j]) # 리스트 뽑아내는 거 생각하기!

set_arr = set(arr)

print(len(set_arr) - 1)
