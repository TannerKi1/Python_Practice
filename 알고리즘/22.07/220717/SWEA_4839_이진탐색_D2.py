T = int(input())

for x in range(1, T+1):
    P, Pa, Pb = list(map(int, input().split()))

    def binary_search(target):
        left = 1
        right = P
        count = 0

        while left <= right:
            mid = (left + right) // 2

            if target > mid:
                left = mid + 1
                count += 1

            elif target < mid:
                right = mid - 1
                count += 1

            if target == mid:
                return count


    def who_is_winner(Pa, Pb):
        if binary_search(Pa) > binary_search(Pb):
            return f'#{x} B'
        elif binary_search(Pa) < binary_search(Pb):
            return f'#{x} A'
        elif binary_search(Pa) == binary_search(Pb):
            return f'#{x} 0'

    print(who_is_winner(Pa, Pb))

