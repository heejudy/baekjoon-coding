num = int(input())
a = list(map(int, input().split()))
maximum = int(input())

left = 0
right = int(max(a))
while left <= right:
    middle = (left + right) // 2
    
    sum = 0
    for i in range(num):
        if a[i] > middle: 
            sum += middle
        else : 
            sum += a[i]

    if sum <= maximum: 
        result = middle 
        left = middle + 1
    else:
        right = middle - 1 

print(result)