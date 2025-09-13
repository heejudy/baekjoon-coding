ls = []
for i in range(9):
    a = input()
    for j in range(9):
        b = int(a.split()[j])
        ls.append(b)
print(max(ls))
if (ls.index(max(ls))+1)%9 == 0:
    print((ls.index(max(ls)))//9+1, 9)
else:
    print((ls.index(max(ls)))//9+1, (ls.index(max(ls))+1)%9)