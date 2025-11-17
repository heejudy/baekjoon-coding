from collections import deque 
cand = int(input())

d = deque([])
for i in range(cand):
    vote = int(input())
    d.append(vote)

dasom = d.popleft()
d = sorted(d)

count = 0
if len(d) == 0:
    count = 0
else:
    while d[-1] >= dasom:
        d[-1] -= 1
        dasom += 1
        count += 1
        d = sorted(d)

print(count)