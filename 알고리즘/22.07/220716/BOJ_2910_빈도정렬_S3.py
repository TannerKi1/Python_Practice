N, C = map(int, input().split())
unsorted_list = map(int, input().split())
answer_dict = dict()

for num in unsorted_list:
    if num not in answer_dict:
        answer_dict[num] = 1
    else:
        answer_dict[num] += 1

sorted_answer = sorted(answer_dict.items(), key = lambda item: item[1], reverse = True)

# for x, y in sorted_answer:


# for key, values in answer_dict.items(key = values):


# 개수를 기준으로 받아서 정렬하는 법 외우기
# dict에서 key값을 자유자재로 이용하기와 같은 말임!