ls = list()
for i in input().split():
    ls.append(int(i))
A = [1, 1, 2, 2, 2, 8]
for j in range(6):
    print(A[j]-ls[j])