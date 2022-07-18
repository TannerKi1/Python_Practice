N = int(input())
empty_list =[]

for _ in range(N):
    char = input()
    empty_list.append(char)

n_empty_list = list(set(empty_list))

# sort 함수를 잘 이해하고 있는지?

# .sort()를 하면 알파벳 순으로 정렬을 해주고
# .sort(len)을 하면 길이 순으로 정렬을 해준다.

# 문제에서는 길이가 우선순위 이기 때문에, 하위 순서인 알파벳을 먼저 불러와주고

#.sort()
#.sort(key = len)으로 하면, 길이 순으로 최종정렬이 이루어지게 된다.

### 중복값을 제거해주고 싶으면 list를 무엇으로 바꿔야 할까? set으로 바꿔야한다. set은 중복값을 허용하지 않는 고유한 값임.

n_empty_list.sort()
n_empty_list.sort(key = len)


for x in n_empty_list:
    print(x)