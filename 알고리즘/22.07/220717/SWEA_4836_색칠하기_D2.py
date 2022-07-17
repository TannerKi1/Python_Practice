# 2차원 컴프리헨션
# 아이디어 빨간색으로 칠해진 곳은 1로 표기
# 파란색으로 칠해진 곳은 2로 표기
# 색깔 안 칠해진 곳은 0

# 그럼 둘 다 겹친 보라색만 2로 표기되게 됨

m, n = 10, 10

red_list = [[0]*m for i in range(n)]
blue_list = [[0]*m for i in range(n)]

print(red_list)
print(blue_list)