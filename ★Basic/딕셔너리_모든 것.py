
# key, value 뒤집어서 저장하는 법

pokedex = {"도룡뇽":1, "망냐뇽":3, "한삼드래":2}

new_pokedex = {y: x for x, y in pokedex.items()}

print(pokedex)
print(new_pokedex)

# dictionary는 key: value의 구조.


# 0부터 9까지 숫자가 몇 개 나왔는지 카운팅 하는 법

k = str(int(input()) * int(input()) * int(input()))

array = [0] * 10

for char in k:
    array[int(char)] += 1

for x in array:
    print(x)

#
