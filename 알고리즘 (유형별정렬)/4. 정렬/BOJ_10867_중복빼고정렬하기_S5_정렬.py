N = int(input())
arr = list(map(int, input().split()))

b = list(set(arr))
b.sort()

for x in b:
    print(x, end = ' ')


# set과 sort쓰면 해결되는 문제.
# sort함수 쓰지 말라고 하면... 머지?