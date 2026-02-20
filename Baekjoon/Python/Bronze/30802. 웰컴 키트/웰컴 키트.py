par = int(input())
A = list(map(int, input().split()))
t, p = list(map(int, input().split()))

count = 0
for i in A:
    if i == 0:
        continue
    else:
        if i <= t:
            count += 1
        else:
            if (i % t) == 0:
                count += (i // t)
            else:
                count += (i // t) + 1

print(count)
print(par//p, par%p)