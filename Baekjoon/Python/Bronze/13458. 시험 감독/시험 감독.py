n = int(input())
n_cnt = list(map(int,input().split()))
b,c = map(int,input().split())
result = 0

for i in range(n):
    n_cnt[i] -= b
    result += 1
    if n_cnt[i] > 0:
        if n_cnt[i] % c == 0:
            result += (n_cnt[i]//c)
        else:
            result += (n_cnt[i]//c+1)

print(result)