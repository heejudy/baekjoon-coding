while True:
    A = sorted(list(map(int, input().split())))

    if A[0] == 0:
        break
    else:
        if A[-1]**2 == A[0]**2 + A[1] **2 :
            print('right')
        else:
            print('wrong')