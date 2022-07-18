word = input()

croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatian:
    word = word.replace(i, '*')

print(len(word))


# 이 문제가 어려워지면... 이제 LeetCode의 Roman to Interger처럼 정해진 Roman 값을 숫자로 리턴해줘야 하는 문제가 되는 것임

