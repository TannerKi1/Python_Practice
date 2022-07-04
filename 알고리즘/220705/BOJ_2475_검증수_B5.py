T = list(map(int, input().split()))

print(sum(([i*i for i in T])) % 10)
