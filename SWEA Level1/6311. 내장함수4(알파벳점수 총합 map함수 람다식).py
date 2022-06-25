
# 풀이 생각해보기

# 문자열을 훑어서, 각각 몇 개 있는지 계산해보고, 개수마다 점수를 곱해서 리턴해준다.

# 근데 이걸 map과, 람다식을 이용해야 한다.


a = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"


# 이건 map을 안 쓰는 방식이긴한데... map을 쓰면서 어떻게 카운트하지?
# map 자체가 한 번 빠르게 훑는 거긴한데.

# a_score = int(a.count('A'))
# b_score = int(a.count('B'))
# c_score = int(a.count('C'))
# d_score = int(a.count('D'))
#
# print((lambda x: 4*x)(a_score)) + int(lambda x: 3*x(b_score)) + int(lambda x : 2*x(c_score)) + int(lambda x: x(d_score)))

# 위의 코드는 개뻘짓. 람다 함수를 아예 이해를 못 하고 있음.
# count를 쓸 거면 그냥 for로 돌려서 for i in a 해서 count 값 올려주면 되지
# if / elif 3개 써서..

# ---------------------------------------------------------
# ord 아스키 값으로... 이게 어떻게 1~4가 된건지는 복습이 필요함
# map 함수자체를 이해를 해야함!
# map(x, y)가 있으면 x에는 함수가 오는 거고, 뒤에 y 자리에는 반복 가능한 자료형이 온다.

print(ord('E'))
print(ord('D'))
print(ord('C'))
print(ord('B'))
print(ord('A'))
print(ord('F'))

# 아스키값이 하나밖에 차이 나지 않는다는 사실을 이용한 원리

list_a = list(a)
b = list(map(lambda x : ord('E') - ord(x), list_a))

# ord에 A가 들어가는 순간, x에는 둘의 차이인 4가 리턴되게 된다.
print(b)
# 그렇게 map 안에는 차례로 , 로 구분된 리스트로 값들이 들어가게 되고...
print(sum(b))
# 그럼 list 내부의 합을 다 더하는 함수인 sum() 을 활용하면 값을 구할 수 있다!


