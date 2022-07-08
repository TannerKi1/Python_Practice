A, B = input().split()

rev_A = A[::-1]
rev_B = B[::-1]

if int(rev_A) > int(rev_B):
    print(int(rev_A))

else:
    print(int(rev_B))
