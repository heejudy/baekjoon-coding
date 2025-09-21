import sys
input = sys.stdin.readline

test_num = int(input())
for _ in range(test_num):
    people_num = int(input())
    
    rank = []
    for _ in range(people_num):
        a, b = (map(int, input().split()))
        rank.append((a, b))


    rank.sort()

    top_ranking = 1e9
    count = 0
    for i in range(people_num):
        if rank[i][1] < top_ranking:
            top_ranking = rank[i][1]
            count += 1
    print(count)