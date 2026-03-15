N = int(input())

count = 0
num = 666

while True:
    str_num = str(num)
    if "666" in str_num:
        count += 1

    if N == count:
        break
    num += 1

print(num)