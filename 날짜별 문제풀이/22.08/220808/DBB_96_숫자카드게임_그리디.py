
N, M = map(int, input().split())

# append로 표기하는 것도 가능
card_deck = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for x in range(N):
    answer = max(answer, min(card_deck[x]))
    # max 함수를 통해, 둘 중 큰 것으로 for문 밖의 answer를 초기화시켜줌

print(answer)





