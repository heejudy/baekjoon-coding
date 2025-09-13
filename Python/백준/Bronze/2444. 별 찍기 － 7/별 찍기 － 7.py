a = int(input())
for i in range(a):
    print(" "*(a-i-1)+"*"*(i+1)+"*"*i)
for j in range(a-1):
    print(" "*(j+1)+"*"*(a-1-j)+"*"*(a-j-2))