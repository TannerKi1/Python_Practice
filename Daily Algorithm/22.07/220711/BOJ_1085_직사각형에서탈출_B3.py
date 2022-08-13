x, y, w, h = map(int, input().split())

# 왼쪽 가로 = x
# 오른쪽 가로 = w-x
# 위쪽 높이 = h-y
# 아래쪽 높이 = y

# 절대값 함수 = abs

list = [x, abs(w-x), abs(h-y), y]
print(min(list))