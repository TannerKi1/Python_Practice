
T = int(input())

for t in range(1, T+1):
    b = list(map(str, input()))
    if b == b[::-1]:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
