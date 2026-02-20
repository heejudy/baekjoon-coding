a = list(map(int,input().split()))

asc = 'ascending'
des = 'descending'
mix = 'mixed'
result = ''
for i in range(0, len(a)-1):
    if a[i+1] - a[i] == 1:
        result = asc
    elif a[i+1] - a[i] == -1:
        result = des
    else:
        result = mix
        break

print(result)