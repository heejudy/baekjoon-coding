K = int(input())
a = []

for i in range(K):
  num = int(input())
  if num == 0:
    a.pop(-1)
  else:
    a.append(num)

sum = 0
for j in a:
  sum += j
print(sum)