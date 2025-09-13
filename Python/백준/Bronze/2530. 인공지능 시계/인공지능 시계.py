h, m, s = map(int, input().split())
sec = int(input())
m1 = sec//60
s1 = sec - m1*60
if 0<=h<24 and 0<=m<60 and 0<=s<60:
    m += m1
    s += s1
    if h>23 or m>59 or s>59:
        m += s//60
        s = s - 60*(int(s//60))
        h += m//60
        m = m - 60*(int(m//60)) 
        if h>23:
            h = h%24
print(h, m, s)