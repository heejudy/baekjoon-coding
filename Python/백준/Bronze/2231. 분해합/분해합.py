result = int(input())
answer = 0

for i in range(1, 1000001):
    a = int(i)
    for j in str(i):
        a+= int(j)

    if a == result:
        answer = i
        break

print(answer)