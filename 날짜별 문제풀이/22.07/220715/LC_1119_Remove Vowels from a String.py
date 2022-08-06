# 모음을 없앤다.

# 리스트 컴프리헨션?


s = "aeiou"

vowel = ['a', 'e', 'i', 'o', 'u']
char = [x for x in s if x not in vowel]

print(''.join(char))

# 개별 문자 하나하나를 char로 쓰는 습관을 들이자. 임의의 문자 배정은 타인과의 협업력을 떨어트린다!