def sit_down(x, lst):
    global cnt

    if x == len(lst):
        print(lst)
        cnt += 1
        return

    if x == 0:
        lst[x] = True
        sit_down(x+1, lst)
        lst[x] = False
        sit_down(x+1, lst)

    if x > 0:
        if lst[x-1] == True:
            lst[x] = False
            sit_down(x+1, lst)

        else:
            lst[x] = True
            sit_down(x+1, lst)
            lst[x] = False
            sit_down(x+1, lst)


n = int(input())
lst = [None] * (n)
cnt = 0

sit_down(0, lst)





