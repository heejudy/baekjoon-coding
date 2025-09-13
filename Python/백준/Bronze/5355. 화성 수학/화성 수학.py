n = int(input())
for i in range(n):
    a = list(input().split())
    k = float(a[0])
    b = a[1:]
    for j in b:
        if j == "@":
            k *= 3
        if j == "%":
            k += 5
        if j == "#":
            k -= 7
    print("{:0.2f}".format(k))