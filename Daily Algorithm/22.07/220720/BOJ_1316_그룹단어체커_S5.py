
N = int(input())

def word_checker(word):

    group_list = [word[0]]
    i = 0
    while i < len(word)-1:
        if word[i+1] != word[i]:
            if word[i+1] not in group_list:
                group_list.append(word[i+1])
                i += 1
            elif word[i+1] in group_list:
                return 0
                break
        elif word[i] == word[i+1]:
            i += 1

    return 1

count = 0
for _ in range(N):
    word = str(input())
    if word_checker(word) == 1:
        count += 1
    else:
        count += 0


print(count)

