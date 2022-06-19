
# binary 함수를 쓰면 되지만... 그래도 계산해보기

# 원리 = 2로 나눈 값을 메모장에 쓰다보면 보임

def binary(num):
    save =[]

    while True:
        a = int(num / 2)
        b = int(num % 2)
        save.insert(0, b)

        if a != num:
            num = a
        else:
            break

    final = ''.join(map(str, save))
    print(final)

num = int(input("10진수 값을 입력해주세요 : "))
binary(num)

