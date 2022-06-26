
# 국어 수학 점수값을 튜플로 저장하고, 각각 튜플을 항목으로 갖는 리스트 객체가 있습니다.

# [(   ,  ),   ( ,   ), ...] 이런 상황이 가정되어있는 것

scores = []
count = int(input("총 학생 수를 입력하세요: "))

# 내부 스코어를 []로 받은 상황

# for i in range(1, count+1):
#     score = []
#     kor = int(input(f'학생{i}의 국어 점수를 입력하세요: '))
#     score.append(kor)
#     math = int(input(f'학생{i}의 수학 점수를 입력하세요: '))
#     score.append(math)
#     scores.append(score)
#
# print(scores)

# 내부 스코어를 튜플로 받는 법은?

# for i in range(1, count+1):
#     score = ()
#     kor = int(input(f'학생{i}의 국어 점수를 입력하세요: '))
#     score.append(kor)
#     math = int(input(f'학생{i}의 수학 점수를 입력하세요: '))
#     score.append(math)
#     scores.append(score)
#
# print(scores)

# 이렇게 하면 오류가 난다. 왜냐. 튜플에는 append라는 함수가 없기 때문. append는 리스트만 쓸 수 있다.
# 그럼 튜플로 받고 싶으면 어떻게 해야할까?

for i in range(1, count+1):
    kor = int(input(f'학생{i}의 국어 점수를 입력하세요: '))
    math = int(input(f'학생{i}의 수학 점수를 입력하세요: '))
    score = (kor, math)
    scores.append(score)


for x in range(0, count):
    print(f'{x+1}번 학생의 총점은 {sum(scores[x])}이고, 평균은 {sum(scores[x])/2}입니다.')

# 이렇게 하면 튜플로 저장할 수 있다....
# 그러면 드는 생각은. 리스트 안에 튜플로 받았을 때와, 리스트 안에 리스트로 받았을 때는 어떠한 차이가 있을까? 등이 생각이 나야한다.

# 출력은 x번 학생의 총점은 a+b 점이고, 평균은 c점입니다. 라는 결과값이 나와야 함.