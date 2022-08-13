
N, M = map(int, input().split())

# append로 표기하는 것도 가능
card_deck = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for x in range(N):
    answer = max(answer, min(card_deck[x]))
    # max 함수를 통해, 둘 중 큰 것으로 for문 밖의 answer를 초기화시켜줌
    # 굳이 list를 만들어서 하나하나 넣어서 공간낭비를 할 필요가 없다

    # list에 일일히 행마다 최소값을 넣어줄 필요없이, 다음 줄로 넘어갈 때 갱신시켜주는 게 나음.

print(answer)





