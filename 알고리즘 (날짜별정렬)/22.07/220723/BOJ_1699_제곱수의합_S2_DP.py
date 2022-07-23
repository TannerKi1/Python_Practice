n = int(input())

d = [0] * (n+1)

for i in range(1, n+1):
    d[i] = i

for k in range(1, n+1):
    for j in range(1, k):
        if j * j > k:
            break
        if d[k] > d[k - j*j] + 1:
            d[k] = d[k - j * j] + 1

print(d[n])

# 가장 큰 제곱수를 기준으로 제곱수를 뺀 값의 카운트에서 + 1
# 기준이 제곱수에서 빼고말고빼고말고.
