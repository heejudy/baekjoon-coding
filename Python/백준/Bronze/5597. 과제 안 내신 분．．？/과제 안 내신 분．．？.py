a = [0]*30

for _ in range(28):
    stu = int(input())
    a[stu-1] = 1


for i in range(30): 
    if a[i] == 0:
        print(i+1) 