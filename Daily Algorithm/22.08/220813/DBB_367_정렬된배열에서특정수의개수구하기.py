# bisect를 쓰면 진짜 빨리 구할 수 있음

from bisect import bisect_left
from bisect import bisect_right

N, target = map(int, input().split())
arr = list(map(int, input().split()))

left_answer = bisect_left(arr, target)
right_answer = bisect_right(arr, target)

if left_answer == right_answer :
    print(-1)
else:
    print(right_answer - left_answer)


