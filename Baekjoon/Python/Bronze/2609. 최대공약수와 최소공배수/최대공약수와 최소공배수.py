import sys
input = sys.stdin.readline

a, b = list(map(int, input().split()))  

def gcd_sol(num):
    lst = []
    for i in range(1, num+1):
        if num % i == 0:
            lst.append(num // i)   
    lst.sort()
    return lst

def gcd(num1, num2):
    lst_a = gcd_sol(num1)
    lst_b = gcd_sol(num2)
    
    max_lst = 0
    for i in lst_a:
        if i in lst_b:
            if i >= max_lst:
                max_lst = i

    return max_lst

def lcm(num1, num2):
    return (num1 * num2) // gcd(num1, num2)

print(gcd(a, b))
print(lcm(a, b))