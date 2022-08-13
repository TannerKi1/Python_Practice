import sys
import math

min_n, max_n = map(int, sys.stdin.readline().split())

# 여기까지 에라토스테네스 체 구현 완료

life = max_n - min_n + 1
arr = [False] * (max_n - min_n + 1)
# for x in range(min_n, int(math.sqrt(max_n)) + 1):
#     for y in prime:


for i in range(2, int(math.sqrt(max_n))+1):
    square = i ** 2
    for j in range((((min_n - 1) // square) + 1) * square, max_n + 1, square):
        #                 4, 8이 선택되고
        if not arr[j - min_n]:
            # arr[3], arr[7]이  True로 빠지게 되나. [0부터 카운팅 되니...] 인쇄하면 4 와 8에 해당하는 자리임.
            arr[j - min_n] = True
            life -= 1 # 이게 더 포인트 1씩 빠진다.

print(life)

# 1 10이라고 치면.

# 에라토스테네스처럼 모든 수를 체크하는 게 아니라, 첫 수를 체크하고 그 수의 배수만 걸러내는 방식.

