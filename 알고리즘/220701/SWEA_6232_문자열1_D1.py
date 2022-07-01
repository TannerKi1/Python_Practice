
#회문 여부를 판단하는 코드 작성하기

T = str(input())
T_list = list(T)

T_list_Reverse = list(T)[::-1]

if T_list == T_list_Reverse:
    print(T)
    print("입력하신 단어는 회문(Palindrome)입니다.")