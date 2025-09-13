b = 0 
while b != 1:
    a = int(input())
    if a == -1:
        b = 1
    else:
        ls = list()
        for i in range(1, a+1):
            if a % i == 0:
                ls.append(i)
        if sum(ls[0:-1]) == a:
            c = ('%d =' %(a))
            for j in ls[0:-1]:
                c += ' %d +' %(j)
            print(c.rstrip(" +"))
        else:
            print("%d is NOT perfect." %(a))