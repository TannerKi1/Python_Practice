A, B = map(int, input().split())

A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

C_set = set(A_arr) & set(B_arr)

print((len(set(A_arr)) - len(C_set)) + (len(set(B_arr)) - len(C_set)))

# set의 시간복잡도를 한번 생각은 해보자.