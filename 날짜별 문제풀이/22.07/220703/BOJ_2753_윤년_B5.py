
N = int(input())

if N % 400 == 0:
    print("1")
if N % 400 != 0 and N % 100 == 0:
    print("0")
if N % 400 != 0 and N % 100 != 0:
    if N % 4 == 0:
        print("1")
    if N % 4 != 0:
        print("0")
