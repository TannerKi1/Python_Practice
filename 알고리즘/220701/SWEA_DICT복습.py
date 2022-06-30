

b = 'abcdefgabc'

myMap = dict()

for char in b:  # b를 독립된 char들로 훑는다. char1 char2 char3...
    if char in myMap:
        myMap[char] +=1
    else:
        myMap[char] = 1

# 특정 알파벳이 처음 들어왔는데, 기존의 히스토리가 없으면 1로 설정되고

# 특정 알파벳이 들어왔는데, 중복된 값이면 그때부턴 카운트 한 개가 더 올라가게 된다.

for key, val in myMap.items():  # myMap.items() / .items() 이건 자주 나오니 잘 사용할 것
    print(f'{key} : {val}')


