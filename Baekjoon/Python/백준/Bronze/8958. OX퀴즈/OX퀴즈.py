n = int(input())
for _ in range(n): 
    ox = input()

    total = 0
    count = 0

    for i in ox:
        if i != 'X':
            count += 1
            total += count 
        else:
            count = 0
            
    print(total)