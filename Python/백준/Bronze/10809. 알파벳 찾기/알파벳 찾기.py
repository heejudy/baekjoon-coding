a = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
t = list()
for i in alpha:
    if i in a:
        A = a.index(i)
        t.append(int(A))
    else: 
        B = -1
        t.append(int(B))
for j in t:
    print(j)