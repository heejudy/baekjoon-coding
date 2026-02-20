s = int(input())
a = 0 
b = 0
if s == 1:
    print(1)
else:
    while b <= s:
        a += 1
        b += a
    print(a-1)