l = list()
for i in range(5):
    a = int(input())
    if a >= 40:
        l.append(a)
    else:
        l.append(40)
print(int(sum(l)/5))