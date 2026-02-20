a = [] 
b = [] 
ls = []
to = 0 
d1 = {'A+':4.5, 'A0':4.0, 'B+': 3.5, "B0":3.0, 'C+':2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
for i in range(20): 
    c = input().split()
    a.append(float(c[1])) 
    b.append(c[-1]) 
for j in range(20):  
    if b[j] != 'P':
        ls.append((a[j])*(d1.get(b[j]))) 
    else:
        a[j] = 0
        b[j] = 'F'
        continue
to = sum(ls)
if sum(a) != 0 and to != 0:
    print('%.6lf' %(float(to)/float(sum(a))))
elif sum(a) == 0:
    print('%.6lf' %0)
else: 
    print('%.6lf' %(float(to)/float(sum(a))))  