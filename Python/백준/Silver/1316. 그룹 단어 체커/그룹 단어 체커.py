N = int(input())

cnt = 0
for i in range(N):
    st = input()

    lst = []
    for i in st:
        if len(lst) == 0:
            lst.append(i)
        if (i in lst) and (lst[-1] != i):
                cnt += 1
                break
        else:
            lst.append(i)
print(N - cnt)