num = int(input())

lst = [0 for i in range(num + 1)]

for i in range(num + 1):
    if i == 0 or i == 1:
        lst[i] = i
    else:
        lst[i] = lst[i - 1] + lst[i - 2]

print(lst[-1])