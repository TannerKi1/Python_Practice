
T = int(input())
b = []
for i in range (1, T+1):
    a = list(map(int, input().split()))
    b.append(a)
    print(f'#{i} {round(sum(a) / 10)}')

print(b)



# round() 함수 사용법 익히기