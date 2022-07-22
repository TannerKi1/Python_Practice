import math
T = int(input())

student = list(map(int, input().split()))
ability_B, ability_C = map(int, input().split())

people = []

for i in range(T):
    major_B = student[i] - ability_B # major_B가 음수로 가는 경우를 막아야한다.
    if major_B <= 0:
        minor_C = 0
    else:
        minor_C = math.ceil(major_B / ability_C)

    people.append(1+minor_C)

print(sum(people))

