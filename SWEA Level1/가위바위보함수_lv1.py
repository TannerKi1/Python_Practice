# 규칙정하기

lv1


def rsp()

a = input("플레이어1의 선택은(가위/바위/보): ")
b = input("플레이어2의 선택은(가위/바위/보): ")

if a == b:
    print("draw!")

if a == '가위' and b == '바위':
    print("플레이어2가 플레이어1을 바위로 이겼습니다.")