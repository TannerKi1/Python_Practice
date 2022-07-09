import math
T = int(input())

student = list(map(int, input().split()))
ability_B, ability_C = input().split()

people = []

for i in range(T):
    major_B = student[i] - int(ability_B)
    people.append(1 + (math.ceil(major_B / int(ability_C))))

print(sum(people))
