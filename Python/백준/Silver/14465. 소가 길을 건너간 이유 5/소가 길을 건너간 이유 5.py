import sys
from itertools import combinations
input = sys.stdin.readline

n, k, b = map(int, input().split())
problem = [0] * n
for _ in range(b):
    error = int(input())
    problem[error-1] = 1  #[1, 1, 0, 0, 1, 0, 0, 0, 1, 1]

psum = [] * (n - k + 1)

problem1 = sum(problem[0:k])
psum.append(problem1)
for i in range(0, n-k):
    problem1 = problem1 - problem[i] + problem[k + i]
    psum.append(problem1)


print(min(psum))