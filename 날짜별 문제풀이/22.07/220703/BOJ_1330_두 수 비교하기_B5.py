
import sys
T = list(map(int, sys.stdin.readline().split()))
A = T[0]
B = T[1]

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")


# sys
# sys.stdin.readline().split() 을 이제 알아두자