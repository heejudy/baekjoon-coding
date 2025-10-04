import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))

psum = [] * (N - K + 1)

a1 = sum(a[0:K])
psum.append(a1)
for i in range(0, N-K):
    a1 = a1 - a[i] + a[K+i]
    psum.append(a1)

print(max(psum))