# # # 숫자열을 받아서, Palindrome인지 검사하는거
# #
# # # str()함수를 알고, [::-1]를 문자열에서도 사용가능하다는 것을 알면 빨리 풀 수 있는데
# #
# # # True, False를 반환하는 문제라면 코드를 더럽게 적지말고
# # 그냥 A==B 하면 Boolean값이 리턴되게 된다. 앞에 지저분하게 if 등을 붙일 이유가 없어짐
# #
# # A = 'apple'
# # B = 'banana'
# #
# # print(A == B)
#
# '------------------------------------'
#
# '아니면 투 포인터 사용해서 가장 왼쪽 값과, 가장 오른쪽 값을 비교해보는 것도 가능!'

w = 'eye'

def if_Palindrome(w):
    l, r = 0, len(w)-1
    while l < r :
        if w[l] != w[r]:
            return False
        l += 1 ; r -= 1
    return True

print(if_Palindrome('eye'))