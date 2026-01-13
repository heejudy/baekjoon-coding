L = int(input())
ls = [i for i in input()]

def has(L, ls):
    result = 0

    for i in range(L):
        od = ord(ls[i]) - 96
        result += od * (31 ** i)
    return result % 1234567891

print(has(L, ls))