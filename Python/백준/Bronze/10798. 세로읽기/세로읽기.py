ls = []
for _ in range(5):
    ls.append([q for q in input()])


ls1 = []
while ls != [[], [], [], [], []]:
    for i in range(5):
        if ls[i] == []:
            continue
        ls1.append(ls[i][0])
        del ls[i][0]
for f in ls1:
    print(f, end = '')