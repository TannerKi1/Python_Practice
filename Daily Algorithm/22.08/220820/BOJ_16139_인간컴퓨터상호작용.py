import sys
input = sys.stdin.readline

n = input()
T = int(input())

for _ in range(T):
    a, b, c = input().split()

    answer = n[int(b):int(c)+1]
    print(answer.count(a))