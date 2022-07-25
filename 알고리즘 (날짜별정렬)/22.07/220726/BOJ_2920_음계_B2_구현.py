
arr = list(map(int, input().split()))

if arr[0] == 1:
    for x in range(1, len(arr)):
        if arr[x] - arr[0] == x:
            continue
        else:
            print('mixed')
            break
    else:
        print('ascending')  # 어제 JB랑 검토했던 구문. if 문을 다 돌고 이상없으면 else에 걸리고, 중간에 else로 빠져서 break으로 빠졌으면 아래 else에는 걸리지 않게 된다.

elif arr[0] == 8:
    for x in range(1, len(arr)):
        if arr[x] - arr[0] == -1 * x:
            continue
        else:
            print('mixed')
            break
    else:
        print('descending')

else:
    print('mixed')




