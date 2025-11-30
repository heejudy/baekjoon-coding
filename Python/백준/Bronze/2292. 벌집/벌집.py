a = int(input())

ls = []
total = 0
count = 1
if a == 1:
    print(1)
else:
    for i in range(1, 20000):
        count += 6 * i
        if a <= count :
            print(i+1)
            break