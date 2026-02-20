import sys

N = int(sys.stdin.readline().rstrip())

d = 2
if N != 1:
    while d <= N:
        if N % d == 0:
            print(d)
            N /= d
        else:
            d += 1