N, M = map(int, input().split())

set_price = []
piece_price = []

for _ in range(M):
    a, b = map(int, input().split())
    set_price.append(a)
    piece_price.append(b)


min_set = min(set_price)
min_piece = min(piece_price)

x = N // 6
y = N % 6

p = (N // 6) + 1
q = 0

c = 0
d = N

print(min(x * min_set + y * min_piece, p * min_set, d * min_piece))


