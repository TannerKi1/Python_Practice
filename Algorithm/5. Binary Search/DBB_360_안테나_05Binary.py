# 집 개수와 안테나 개수
n, c = map(int, input().split())

# 집의 위치 정보
array = []

# 집 위치 정보 저장
for i in range(n):
    array.append(int(input()))

# 오름차순으로 정렬
array.sort()

# 최소 거리와 최대 거리 구하기
start = 1
end = array[-1] - array[0]

result = 0

# 최적 설치거리 파악을 위한 while문 선언
while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1

    for i in range(1, n):
        # 만약 정한 최소거리보다 더 넓게 설치가 가능하다면,
        if array[i] >= value + mid: # mid라는 값이 집과 집 사이의 거리임을 알 수 있다.
            count += 1
            value = array[i]

    # 모든 집에 대해 안테나 설치 여부 파악이 끝난 뒤, 정해진 개수보다 많이 설치했다면 최소 거리를 너무 짧게 잡은 것이므로 최소 거리를 늘려준다.
    # 너무 많이 설치했어도 최소 거리를 늘려야하고, 혹시 딱 맞게 설치했어도 더 거리를 늘려봐도 될 수도 있기 때문에 반복해준다.
    if count >= c:
        start = mid + 1
        result = mid

    # 정해진 개수보다 적게 설치했다면, 너무 최소 거리를 길게 잡은 것이므로 최소 거리를 좁혀준다.
    else:
        end = mid - 1

# start가 커지거나, end가 작아지거나를 반복하면서 결국 start와 end는 같아지는 순간이 올 때, 저장된 result값이 최적이다.

print(result)

# 예를 들어, (36, 42, 39), (40, 42, 41), (40, 40, 40) 인 상황에서 이미 최적해는 39로 결정이 나고 나머지 41, 40이 제시되었더라도
# 그 값이 갱신이 되어서는 안 됨.



