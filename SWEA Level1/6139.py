# 회문 체크하는 프로그램 만들기

# 내가 생각한 원리
# 문자를 받는다

word = (input("아무 영어 단어를 입력해주세요: "))

a = list(map(str, word))

# 문자를 뒤집어 본다.

b = a[::-1]

# 둘을 비교한다
# 같으면, 회문입니다. 틀리면 아닙니다를 출력

if a == b:
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print("회문이 아니야")

