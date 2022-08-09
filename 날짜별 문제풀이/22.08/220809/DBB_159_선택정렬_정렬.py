arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)): # 시작점 바로 오른쪽부터 시작해 오른쪽으로 쭉 가겠다.
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]  # 이건 특이하게 결과값이 뒤에 껄로 바뀌게 됨
    print(arr)
print(arr)

# 파이썬 스와프 소스코드 이해하기
# 가장 처음 0과 7의 위치가 바뀐 것을 알 수 있다.