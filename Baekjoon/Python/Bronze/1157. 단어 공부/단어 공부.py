a = input().upper()
b = set()
for i in a:
    b.add(i)    

c = []
for j in list(b):
    c.append(a.count(j))
if c.count(max(c)) > 1:
    print('?')
else:    
    print(list(b)[c.index(max(c))])