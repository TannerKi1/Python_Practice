import sys

lines = sys.stdin.readlines()

for line in lines:
    A, B = map(int, line.split())
    print(A+B)
    print(type(map(int, line.split())))

# EOF 엔드 오브 파일 처리를 어떻게 할 것인지.

# sys.stdin.readlines()로 모든 줄을 끝까지 당겨온다.

# for 문으로 하나하나 돌려본다.
# 돌릴 때, 그냥 가져온 값을 split으로 나눠주고 int값으로 변환해준다.
