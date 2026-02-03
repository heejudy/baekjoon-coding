import sys

input = sys.stdin.readline

tree_num, tree_need = list(map(int, input().split()))
tree_lst = list(map(int, input().split()))

end = max(tree_lst)
start = 0

while start <= end:
    middle = (start + end) // 2
    total = 0

    for i in tree_lst:
        if i > middle and total < tree_need:
            total += i - middle
    if total >= tree_need:
        start = middle + 1
    else:
        end = middle - 1
print(end)