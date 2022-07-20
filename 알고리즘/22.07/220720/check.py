

N = str(input())

count = 0

num_list = [int(x) for x in N]


for i in range(len(num_list)-2):
    if num_list[i]-num_list[i+1] == num_list[i+1] - num_list[i+2]:
        print(num_list[i] - num_list[i+1])
        continue
    elif num_list[i] - num_list[i+1] != num_list[i+1] - num_list[i+2]:
        print("등차수열이아닙니다")
        break

