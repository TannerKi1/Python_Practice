# pokedex = {"도룡뇽":1, "망냐뇽":3, "한삼드래":2}
#
# sorted_pokedex = sorted(pokedex.items(), key = lambda x: x[1])


k = str(int(input()) * int(input()) * int(input()))

array = [0] * 10

for char in k:
    array[int(char)] += 1

for x in array:
    print(x)


# dictionary는 값이 들어오지 않으면 value값을 0으로 저장하지 않는다.

