

# 원리는... dic은 key, value 있으면, key가 들어오면 리스트랑 다르게 카운트가 탁 올라가는 그건데...

# 사실 count 함수 쓰면 됨.

b = 'abcdefgabc'

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
c = [0] * len(a)

# 그냥 아는대로 리스트로 풀어보기

for x in b:
    for j in range(1, len(a)+1):
        if x == a[j-1]:
            c[j-1] += 1

for i in range(1, len(a)+1):
    print(f'{a[i-1]},{c[i-1]}')




# 분명히 dic으로 푸는 방법이 있을건데!!!!!


