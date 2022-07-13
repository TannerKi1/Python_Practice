s = "0P"

s_lower = s.lower()
list_ = []
for x in s_lower:
    if 'a' <= x <= 'z':
        list_.append(x)
    elif '0' <= x <= '9':
        list_.append(x)

if list_ == list_[::-1]:
    print("True")

else:
    print("False")


# 테케 통과

# 숫자 부분을 정의해주지 않으면 정답을 찾을 수 없었던 문제
# Runtime 상위 39%.

# 참고하기(1)
# .isalnum() 함수를 활용가능하다.
# .isalnum() 을 이용하면, a~z 값과, 0~9의 값을 따로 잡았던 걸 깔끔한 코드로 줄일 수 있다.

# 참고하기(2) - Two pointer solution
# 투포인터로 왼쪽 맨 끝고, 오른쪽 맨 끝에서부터 출발해 이 문제를 풀의한 풀이가 있다.
# 투포인터는 반드시 인지하도록 하자

cama!c
왼쪽, 오른쪽에서 접근

만약 isalnum이 아니면, 왼쪽에선 오른쪽으로 하나 보내고, 오른쪽에선 왼쪽으로 하나 보내주고

### 참고 코드 ###
# 안 보고 아래와 같이 투 포인터 작성할 수 있어야 함
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True