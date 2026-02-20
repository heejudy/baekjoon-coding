N = int(input())
K = []
t = []
for i in range(N):
    A = input()
    fir = int(A.split()[0])
    sec = int(A.split()[1])
    K.append(fir+sec) 
    C = "Case #%d: " %(i+1) 
    t.append(C + str(K[i]))
for j in t:
    print(j)