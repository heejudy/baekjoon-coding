str = input()
result = ''
for i in str:
    if ord(i) <= 91:
        result += i.lower()
    else:
        result += i.upper()
print(result)