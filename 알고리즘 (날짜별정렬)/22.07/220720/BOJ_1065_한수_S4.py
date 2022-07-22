# 아이디어

# 각자리 수를 str으로 받은 다음 다시 int로 변환해

# a[0] - a[i] =! 이런 걸로 끝가지 같으면 받고
# 중간에 != 뜨면 break 뜨면서 while 탈출시키기

N = int(input())

def checker(x):
    num_list = list(map(int, str(x)))
    i = 0
    if len(num_list) <= 2:
        return 1
    if len(num_list) >= 3:
        while (i + 2) <= (len(num_list) - 1) :
            if num_list[i] - num_list[i+1] != num_list[i+1] - num_list[i+2]:
                return 0
            else:
                i += 1
        return 1

count = 0

for x in range(1, N+1):
    if checker(x) == 1:
        count += 1

print(count)

