
# 역으로 투포인터 가능?
# 일단 list가 아니기 때문에 string을 쪼개서 리스트로 받아본다.

s = 'leetcode'

char = [x for x in s]

l, r = 0, len(char) - 1
vowel = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]

while l < r:
    if char[l] not in vowel:
        l += 1
    elif char[r] not in vowel:
        r -= 1
    elif char[l] in vowel and char[r] in vowel:
        char[l], char[r] = char[r], char[l]
        l += 1
        r -= 1

    print(''.join(char))


