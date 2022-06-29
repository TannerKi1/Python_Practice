# 아래의 상품 딕셔너리 데이터를 가격에 따라 내림차순으로 정렬하는 프로그램을 작성하십시오.
#
my_dict = {"TV": 2000000, "냉장고": 1500000, "책상": 350000, "노트북": 1200000, "가스레인지": 200000, "세탁기": 1000000}

sorted_dict_2 = sorted(my_dict.items(), key = lambda item: item[1], reverse = True)

print(my_dict.items())

sorted_dic_3 = sorted(my_dict.items(), key = lambda item: item[0], reverse = False)

print(sorted_dic_3)

# 튜플 안의 값을 특정 기준으로 오름차순, 내림차순하는 연습문제라고 할 수 있다.
# my.dict.items()가 무엇인지 부터 정리를 해야한다.
# dict_items 뒤에 튜플 값을 반환해준다.
# 여기에서 key item[0]은 품목이고, key item[1]은 가격이다.
print("---*5")
b = list(sorted_dict_2)
for m, k in b:
    print(f'{m}: {k}')

# b라는 튜플값을 분리해서 사용하고 싶을 때 사용하는 방식을 알아두자