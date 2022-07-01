

# URL 주소를 구분하래

# 뭔가 '/'를 기준으로 슬라이싱 하는 것 아닐까?

# find 함수를 써보자. http 뒤는 왼쪽부터, 뒤쪽은 rfind를 쓰면 될 것 같다.

k = 'http://www.example.com/test?p=1&q=2'

a = k[0:k.find(':', 0)]
b = k[k.find('w', 0) : k.rfind('/', 0)]
c = k[k.rfind('/', 0)+1:]

print(f"protocol: {k[0:k.find(':', 0)]}")
print(f'host: {b}')
print(f'others: {c}')



# f 스트링에서 ' 랑 " 잘 구분해주자