def solution(idx, n, lst):
    global answer

    if idx == n:
        print(lst)
        answer += 1
        return

    if idx == 0:
        lst[idx] = True
        solution(idx + 1, n, lst)
        lst[idx] = False
        solution(idx + 1, n, lst)

    else:
        if lst[idx - 1] == True:
            lst[idx] = False
            solution(idx + 1, n, lst)
        else:
            lst[idx] = True
            solution(idx + 1, n, lst)
            lst[idx] = False
            solution(idx + 1, n, lst)

answer = 0
n = 3
solution(0, n, [[None] for _ in range(n)])

print(answer)