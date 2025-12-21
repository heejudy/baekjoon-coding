a = input() 

result = ''
for i in a:
    if i.lower() == i:
        result += i.upper()
    else:
        result += i.lower()

print(result)