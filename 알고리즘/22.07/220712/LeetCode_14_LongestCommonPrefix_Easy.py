# 아이디어
# a[0] 의 문자와 a[1]의 문자를 비교한다. 같으면... a[2]와도 비교한다.... 끝까지 i가 있으면 j, j의 값을 +1 시켜준다.
# len의 끝까지 돌았는데 모두가 같으면 그 문자를 ''안에 + 해준다.
# 중간에 !=가 나오는 순간 종료된다.

strs = ["flower","flow","flight"]
len_strs = [len(x) for x in strs]
j_limit = min(len_strs)
# a[i][0], a[i+j+1][0], a[i+j+2][0] 이 같은지 체크 만약에 끝까지 같다, 그러면 바구니에 담긴다
# a[1][0], a[i][1]이 같은지 체크

# i도 올라가야하고, j도 올라가야하는데, 어디까지 올라갈 수 있을지가 고민. i는 단어의 개수까지 올릴 수 있고, j의 경우에는 가장 짧은 단어까지만 체크하면 됨.

for i in range(j_limit):
    for j in range(len(strs)):
        k = 1
        while j+k < len(strs):
            if strs[j][i] == strs[j+k][i]:
                print("값을 1증가시킵니다")
                k += 1
            else:
                print("여기서 종료되었습니다.")
                break


# 그럼 가장 짧은 단어가 몇 개를 가지는지는 어떻게 확인?
# map함수를 이용해서 다 len값으로 전환..?



# 단어 자체의 체크 여부는 len-1까지만 체크하면 된다는 결론이 나온다.