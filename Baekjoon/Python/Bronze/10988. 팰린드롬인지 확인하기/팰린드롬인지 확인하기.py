a = input()
ls = list()
for i in a:
    ls.append(i)
als = ls.copy()   
ls.reverse()
if als == ls :
    print(1)    
else:
    print(0)