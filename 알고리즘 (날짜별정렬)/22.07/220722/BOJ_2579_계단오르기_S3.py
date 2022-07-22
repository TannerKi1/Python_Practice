

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