a, p = list(map(int, input().split()))  

total = []
total.append(a)

def sum_mul(num):
    st_num = str(num)
    Dn = 0
    for i in range(len(st_num)):
        Dn += int(st_num[i])**p

    return Dn

check = True
while check:
    result = sum_mul(total[-1])

    if result in total:
        stop = total.index(result)
        print(stop)
        check = False
    else:
        total.append(result)