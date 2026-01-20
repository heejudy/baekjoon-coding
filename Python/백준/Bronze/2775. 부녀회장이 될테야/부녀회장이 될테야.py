import sys
input = sys.stdin.readline

test_case = int(input())

all_people = [[0] * 15 for _ in range(15)]
for i in range(15):
    for j in range(15):
        if i == 0:
            all_people[i][j] = j + 1
        elif j == 0:
            all_people[i][j] = 1
        else:
            all_people[i][j] = all_people[i-1][j] + all_people[i][j-1]

for _ in range(test_case):
    k = int(input())
    n = int(input())

    print(all_people[k][n - 1])