# for문 입력
# arr(리스트)의 길이만큼 출력해야하는 상황.

arr = [1, 2, 3, 4, 5]
x = "안녕하세요"

# arr.set(1, 5) 그런데 이건 이미 index 1 값이 정해져있어야 한다.

arr.append(5)
# arr.add(6)

k = arr[0]
#arr.get(0) get뒤에는 index값이 들어가게 됨.

sub_arr = arr[1:4]
# arr.sublist(1,4)

print(arr)
print(k)
print(sub_arr)


# 5번 나오게 된다.
# 자바로 적어보자면...

# 물론 x는 String x 로 사전정의가 되어있어야함.
'''
for (int i = 0; i < arr.length(); i++){
    System.out.println(x)
}


'''