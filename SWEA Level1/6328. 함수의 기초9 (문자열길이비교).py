

# len을 써서 비교해서 긴 걸 return하면 되지 않을까?

# 근데 인자로 전달된 2개니까, list(map) 써서 쪼개줘야한다.

def comp(char1, char2):
    if len(char1) > len(char2):
        print(char1.strip())
    else:
        print(char2.strip())

char1, char2 = list(map(str, input().split(',')))

comp(char1, char2)


#이거 오답뜨는 건 three 앞에 공백 하나 있어서 그렇다.
# 따라서 공백을 없어주는 어떤 함수를 사용해야 한다.
# .strip()을 활용하자