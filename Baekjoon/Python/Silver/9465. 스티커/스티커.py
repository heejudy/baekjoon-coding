test_case = int(input())

for _ in range(test_case):
    n = int(input())
    sticker = [[],[]]
    for i in range(2):
        sticker[i] = list(map(int, input().split()))

    max_list = [[0]*n for _ in range(2)]

    max_list[0][0] = sticker[0][0]
    max_list[1][0] = sticker[1][0]

    if n > 1:
        max_list[0][1] = sticker[0][1] + max_list[1][0]
        max_list[1][1] = sticker[1][1] + max_list[0][0]

    for i in range(2, n):
        max_list[0][i] = sticker[0][i] + max(max_list[1][i-1], max_list[1][i-2])
        max_list[1][i] = sticker[1][i] + max(max_list[0][i-1], max_list[0][i-2])

    print(max(max_list[0][n-1], max_list[1][n-1]))