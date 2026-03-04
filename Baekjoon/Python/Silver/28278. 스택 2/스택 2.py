import sys
input = sys.stdin.readline

stack = []
result = []

for i in range(int(input())):
    a = input().split()

    if a[0] == "1":
        stack.append(int(a[1]))
    
    elif a[0] == "2":
        result.append(stack.pop() if stack else -1)
    
    elif a[0] == "3":
        result.append(len(stack))
    
    elif a[0] == "4":
        result.append(0 if stack else 1)
    
    else:
        result.append(stack[-1] if stack else -1)

for i in result:
    print(i)