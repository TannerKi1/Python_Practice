N = str(input())
import math

arr = [0] * 10

for x in N:
    if x == '6':
        arr[int(6)] += 0.5
    elif x == '9':
        arr[int(6)] += 0.5
    else:
        arr[int(x)] += 1

print(math.ceil(max(arr)))

# 백준에서도 math 인식은 함. 그런데 파이썬 고질병 2.5 round를 2로 내리는 건 어떻게 해결해야 할지 고민은 해봐야함..

