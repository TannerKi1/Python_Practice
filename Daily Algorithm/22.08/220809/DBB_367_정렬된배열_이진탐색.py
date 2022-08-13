# 이방법은 lonN이 아니라 N이 걸리게 된다?

import time
start = time.time()
n, k = map(int, input().split())

arr = list(map(int, input().split()))

dict_1 = dict()

for num in arr:
    if num not in dict_1:
        dict_1[num] = 1
    else:
        dict_1[num] += 1

if k in dict_1.keys():
    print(dict_1[k])
else:
    print(-1)

## 다른 방법. 이진 탐색 2번 해서 특정값의 시작 인덱스와 끝 인덱스 바로 알아내기