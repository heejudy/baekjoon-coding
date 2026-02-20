a = input() 
b = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in b:
    if i in a:
        a = a.replace(i,'b')
print(len(a))