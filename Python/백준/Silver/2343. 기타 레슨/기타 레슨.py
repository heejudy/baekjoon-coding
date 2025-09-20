N, M = map(int, input().split())
lec = list(map(int, input().split()))

left = max(lec)
right = sum(lec)
result = right 
while left <= right:
    middle = (right + left) // 2

    newlist = list()

    sum = 0
    for i in (lec):
        if middle >= sum + i:
            sum += i
        else: 
            newlist.append(sum)
            sum = i
    newlist.append(sum)
        
    
    if len(newlist) > M:
        left = middle + 1
    else: 
        result = middle 
        right = middle - 1

print(result)