WORD = input()

count = len(WORD) // 10
last = len(WORD) % 10

for i in range(0, count+1):
    print(f'{WORD[0+10*i:10+10*i]}')