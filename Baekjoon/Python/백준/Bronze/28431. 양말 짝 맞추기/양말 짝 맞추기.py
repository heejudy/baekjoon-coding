ls = list()
de = set()

for _ in range(5):
    ls.append(int(input()))

for i in ls:
    if ls.count(i) == 3:
        de.add(i)
    elif ls.count(i) >= 2:
            de.add(i)

while len(ls) != 1:
    for i in de:
        ls.remove(i)
print(ls[0])