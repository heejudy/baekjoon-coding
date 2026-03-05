import sys
input = sys.stdin.readline

for i in range(int(input())):
    count = [0, 0, 0, 0]
    change = int(input())

    while change >= 1:
        if change >= 25: 
            count[0] += 1
            change -= 25
        elif change >= 10:
            count[1] += 1
            change -= 10
        elif change >= 5:
            count[2] += 1
            change -= 5
        else:
            count[3] += 1
            change -= 1

    for i in count:
        print(str(i), end = ' ')
