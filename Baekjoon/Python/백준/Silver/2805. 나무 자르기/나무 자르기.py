n,m = map(int,input().split())
trees = list(map(int,input().split()))
trees.sort()
s=0
e=trees[n-1]
mid = 0
while s <= e:
    mid = (s+e)//2
    # mid 높이로 잘라보기
    sum = 0
    for tr in trees:
        if tr > mid: # 잘리는 부분 있음
            sum += tr-mid
    # 조건 체크
    if sum >= m:
        s = mid+1
    else:
        e = mid-1
print(e)