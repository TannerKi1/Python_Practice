
# 카운트 다운하는 함수를 정의해야함.
# if랑 while의 위치를 신경쓰자. indent가 어딨느냐에 따라서 0을 넣었을 때의 결과값이 맨 위 혹은 만 아래로 나오게 된다.
# n이 들어오면 while로 0보다 클 때는 -1 하면서 값을 리턴해준다
# 대신에 n에 0보다 작은 값이 나오면 오류 값을 프린팅해준다.


def countdown(n):

    if int(n) <= 0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")

    while int(n) > 0:
        print(n)
        n -= 1

        # if int(n) == 0:
        #     print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")

countdown(0)
countdown(10)
