import sys

while True:
    a = str(sys.stdin.readline().strip())
    if a == '0':
        break
    else:
        if a[::-1] == a:
            print("yes")
        else:
            print("no")