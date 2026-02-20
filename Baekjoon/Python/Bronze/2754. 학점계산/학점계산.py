grade = input() 

if grade == "F":
    print(0.0)
else:
    result = 0
    result += 69 - ord(grade[0])
    if grade[1] == '+':
        result += 0.3
    elif grade[1] == '-':
        result -= 0.3

    print(float(result))