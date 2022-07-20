# 아이디어

# 각자리 수를 str으로 받은 다음 다시 int로 변환해

# a[0] - a[i] =! 이런 걸로 끝가지 같으면 받고
# 중간에 != 뜨면 break 뜨면서 while 탈출시키기

N = str(input())
num_list = list(map(int, N)) # 리스트랑 맵이용해서 자유자재로 바꾸기

def checker(num_list):

