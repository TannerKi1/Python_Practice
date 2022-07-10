import math

A, B, V = map(int, input().split())

pre_answer = math.ceil((V-A) / (A-B))

print(pre_answer+1)