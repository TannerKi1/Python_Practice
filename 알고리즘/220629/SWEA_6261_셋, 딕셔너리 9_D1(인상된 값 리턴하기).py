
# 기존 dic의 value 값을 5% 인상해서 리턴하는 dic2를 만들어야 하는 상황


beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}

# 어떤 걸 해서

beer_2 = {j: k*1.05 for j, k in beer.items()}

print(beer, "# 인상 전")
print(beer_2, "# 인상 후")

