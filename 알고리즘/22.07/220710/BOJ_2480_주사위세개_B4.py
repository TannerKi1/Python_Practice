# 분명 더 나은 방법이 있겠지만
# 브론즈 4처럼 풀어보자

A, B, C = map(int, input().split())
arr = [A, B, C]

if A == B == C:
    print(10000 + A*1000)

elif A == B != C:
    print(1000 + A*100)

elif A != B == C:
    print(1000 +B*100)

elif A == C != B:
    print(1000 + A*100)

elif A != B != C:
    print(max(arr)*100)