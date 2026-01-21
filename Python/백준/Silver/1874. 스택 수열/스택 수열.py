import sys
input = sys.stdin.readline

N = int(input())
to_make_list = []
for _ in range(N):
    to_make_list.append(int(input()))

comp = []
result = []

point = 1
rem = 0

while rem < N:
    if comp and comp[-1] == to_make_list[rem]:
        comp.pop()
        result.append('-')
        rem += 1
    else:
        if point <= N :
            comp.append(point)
            result.append('+')
            point += 1
        else:
            print("NO")
            sys.exit()
for i in result:
    print(i)