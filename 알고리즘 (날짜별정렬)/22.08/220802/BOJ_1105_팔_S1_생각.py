L, R = map(str, input().split())

if len(L) != len(R):
    print(0)

else:
    cnt = 0
    for i in range(0, len(L)):
        if L[i] != R[i]:
            break

        elif L[i] and R[i] == '8':
            cnt += 1
    print(cnt)



