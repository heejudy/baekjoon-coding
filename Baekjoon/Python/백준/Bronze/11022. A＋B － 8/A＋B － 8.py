T = int(input())
K = []
for i in range(T):
    A = input()
    A1 = int(A.split()[0])
    A2 = int(A.split()[1])
    t = "Case #%d: %d + %d = %d" %(i+1, A1, A2, A1+A2)
    K.append(t)
for j in K:
    print(j)