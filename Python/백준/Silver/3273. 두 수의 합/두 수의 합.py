list_len = int(input())
input_list = list(map(int, input().split()))
target_num = int(input())

input_list.sort() 

count = 0
start, end = 0, list_len - 1
while start < end:
    if input_list[start] + input_list[end] == target_num:
        count += 1
        start += 1
        end -= 1
    elif input_list[start] + input_list[end] > target_num:
        end -= 1
    else:
        start += 1

print(count)