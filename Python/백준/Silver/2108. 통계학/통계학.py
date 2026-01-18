#2108
import sys
input = sys.stdin.readline

N = int(input())
ls = [int(input()) for _ in range(N)]

def avg(num, list_num):
    return int(round(sum(list_num)/num, 0))

def mid(num, list_num):
    list_num.sort()
    return list_num[num//2]

def freq(list_num):
    list_num.sort()
    dt = dict()
    for i in list_num:
        if i in dt:
            dt[i] += 1
        else:
            dt[i] = 1

    max_count = max(dt.values())    
    modes = [k for k, v in dt.items() if v == max_count]
    
    if len(modes) == 1:
        return modes[0] 
    else:
        return modes[1]

def ran(list_num):
    return max(list_num) - min(list_num)

print(avg(N, ls))
print(mid(N, ls))
print(freq(ls))
print(ran(ls))