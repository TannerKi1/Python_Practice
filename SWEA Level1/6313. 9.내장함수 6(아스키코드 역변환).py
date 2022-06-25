
# ord는 문자를 받으면 숫자를 return

# chr는 숫자를 받으면 문자를 return


def a_trs():
    c = int(input("어떤 문자로 변환할까요?: "))
    d = chr(c)

    print(f'ASCII {c} => {d}')

a_trs()