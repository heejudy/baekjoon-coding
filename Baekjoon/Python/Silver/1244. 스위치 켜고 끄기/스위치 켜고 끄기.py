import sys

count = int(input())
switch = list(map(int, sys.stdin.readline().rstrip().split()))
student = int(input())
for i in range(student):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    a[1] >= 1
    if a[0] == 1:
        qotn = a[1]
        while 1 <= qotn <= count:
            switch[qotn-1] = abs(switch[qotn-1]-1)
            qotn += a[1]
    else:
        switch[a[1]-1] = abs(switch[a[1]-1]-1)
        for j in range(count):
            if 1 <= a[1]-j and a[1]+j < count+1:
                if switch[a[1]-j-1:a[1]+j] == switch[a[1]-j-1:a[1]+j][::-1]:
                    switch[a[1]-j-1] = abs(switch[a[1]-j-1]-1)
                    switch[a[1]+j-1] = abs(switch[a[1]+j-1]-1)
            else: 
                break

divide = count//20

a = ""
if divide > 0:
    idx = 0
    for k in range(divide):
        for __ in switch[k*20 : 20*(k+1)]:
            a += str(__)
            a += " "
        print(a.rstrip())
        idx += 1
        a = ""
    for _ in switch[idx*20:]:
        a += str(_)
        a += " "
    print(a.rstrip())
else: 
    for ___ in switch:
        a += str(___)
        a += " "
    print(a.rstrip())