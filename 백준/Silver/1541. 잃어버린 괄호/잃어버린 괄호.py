input_data = input()

# 숫자, 연산자 분리 
lst = []

a = ''
for i in range(len(input_data)):
    if input_data[i] == '-' or input_data[i] == '+':
        lst.append(int(a))
        lst.append(input_data[i])
        a = ''
    else: 
        a += str(input_data[i])
lst.append(int(a))

i = 0
while i < len(lst):
    # + 계산
    if lst[i] == '+':
        wait = lst[i-1] + lst[i+1]
        lst[i-1:i+2] = [wait]
        i -= 1 
    else:
        i += 1

# - 계산
i = 0
while i < len(lst):
    if lst[i] == '-':
        wait = lst[i-1] - lst[i+1]
        lst[i-1:i+2] = [wait]
        i -= 1
    else:
        i += 1

print(lst[0])