

n = int(input())
stairs = []
dp = []
for i in range(n):
    stairs.append(int(input()))

if n==1:
    print(stairs[0])
    exit()
elif n == 2:
    print(max(stairs[0]+stairs[1], stairs[1]))
    exit()

dp.append(stairs[0])
dp.append(stairs[0] + stairs[1])
dp.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))

for i in range(3, n):
    dp.append(stairs[i] + max(dp[i-2], dp[i-3]+stairs[i-1]))

print(dp[-1])




####이하 틀렸던 코드. 위의 코드랑 비교해서 뭐가 차이나는 거지?

# 메뚜기전사랑 비슷해보이는데?

n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

# 여기까지 계단 목록 만들었고.

d = []# 300이하의 자연수라 했으니.
d.append(array[0])
d.append(array[0] + array[1])
d.append(max(array[0]+array[2], array[1] + array[2]))

for i in range(3, n):
    d.append(array[i] + max(array[i - 1] + d[i - 3], d[i - 2]))

print(d[-1])
print(d[1])