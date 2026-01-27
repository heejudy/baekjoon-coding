a = int(input())
lst = [0 for i in range(a + 1)]

def fib(n):
    if n > 0:
        lst[1] = 1
        for i in range(2, n + 1):
            lst[i] = lst[i - 1] + lst[i - 2]
    return lst[n]
    
print(fib(a))