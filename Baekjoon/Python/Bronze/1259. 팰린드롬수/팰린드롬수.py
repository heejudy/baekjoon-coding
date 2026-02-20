from collections import deque

boo = True

while boo:
    a = input()
    st = deque(i for i in a)
    if a == '0':
        boo = False
    else:
        while len(st) > 1:
            if st[0] == st[-1]:
                st.popleft()
                st.pop()
            else:
                print("no")
                break
        if len(st) == 1 or len(st) == 0:
            print("yes")
    