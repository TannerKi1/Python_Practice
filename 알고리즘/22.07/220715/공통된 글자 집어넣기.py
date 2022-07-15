

words = ['flower', 'fly', 'flag', 'flu']


len_words = [len(x) for x in words]

check_num = min(len_words)
res = ''

for x in range(0, check_num):
    for y in range(0, len(words)-1):
        res += words[y][x]
        if words[y][x] != words[y+1][x]:
            break
print(res)

