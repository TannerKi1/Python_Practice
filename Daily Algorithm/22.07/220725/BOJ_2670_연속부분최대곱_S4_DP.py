T = int(input())

arr = []
for _ in range(T):
    arr.append(float(input()))

# 1.0 보다 작아지면 기회 박탈. 시작점을 리셋해야함.

for i in range(1, len(arr)):
    arr[i] = max(arr[i-1] * arr[i], arr[i])

    # 이렇게 하면 나랑 곱해서 작아지는 값은 버리고 다시 내가 기준이 되게 됨. 오히려 곱셈이어서 더 간단?

print(f'{max(arr):.3f}')


# ----------------------- #


# T = int(input())
#
# arr = []
# for _ in range(T):
#     arr.append(float(input()))
#
# # 1.0 보다 작아지면 기회 박탈. 시작점을 리셋해야함.
#
# d = [1.1] 함부로 값 넣지 말것!
# for i in range(1, len(arr)):
#     d.append(max(d[i-1]*arr[i], arr[i]))
#
#     # 이렇게 하면 나랑 곱해서 작아지는 값은 버리고 다시 내가 기준이 되게 됨. 오히려 곱셈이어서 더 간단?
#
# print(f'{max(d):.3f}')
