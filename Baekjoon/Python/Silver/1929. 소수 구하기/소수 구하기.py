low, high = list(map(int, input().split()))

check_list = [True] * (high + 1)
check_list[0] = check_list[1] = False

for i in range(2, int(high ** 0.5) + 1):
    if check_list[i]:
        for j in range(i * i, high + 1, i):
            check_list[j] = False

for i in range(low, high + 1):
    if check_list[i]:
        print(i)