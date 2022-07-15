# 모음을 없앤다.

# 리스트 컴프리헨션?


s = "aeiou"

vowel = ['a', 'e', 'i', 'o', 'u']
char = [x for x in s if x not in vowel]

print(''.join(char))
