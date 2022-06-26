

import random

# def lotto_program():
#     print("청소 당번을 뽑아 봅시다")
#     a = int(input("시작 번호를 입력해 주세요: "))
#     b = int(input("끝 번호를 입력해 주세요: "))
#     c = int(input("공은 총 몇 개를 뽑아 볼까요?: "))
#
#     lotto_a = random.sample(range(a, b+1, 1), c)
#     print(f'행운의 번호는 총 {c}개이며, 모두 {sorted(lotto_a)}입니다.')
#
# lotto_program()


# 시작도 함수로 구현한다면??/

def input_start():
    start = 0
    try:
        start = int(input("로또 번호의 시작 번호를 입력하세요: "))
    except:
        start = 1
    finally:
        return start

def input_end():
    end = 0
    try:
        end = int(input("로또 번호의 끝 번호를 입력하세요: "))
    except:
        end = 45
    finally:
        return end

def input_count():
    count = 0
    try:
        count = int(input("로또 공의 개수를 입력하세요: "))
    except:
        count = 6
    finally:
        return count


def print_lotto(start, end, count):
    lotto = random.sample(range(start, end+1, 1), count)
    print(lotto)