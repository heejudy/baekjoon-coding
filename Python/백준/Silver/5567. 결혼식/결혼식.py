friend = int(input())
list_num = int(input())

friend_num = [[] for _ in range(friend)]

for _ in range (list_num):
    rel = list(map(int, input().split()))
    friend_num[rel[0]-1].append(rel[1])
    friend_num[rel[1]-1].append(rel[0])

total = []
total.extend(friend_num[0])
for i in friend_num[0]: # 2, 3
    total.extend(friend_num[i-1])

result = set(total)
result.discard(1)   

print(len(result))