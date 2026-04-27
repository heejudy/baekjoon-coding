
def solution(clothes):
    answer = 0
    
    dic = dict()
    for i in clothes:
        if not i[1] in dic:
            dic[i[1]] = 1
        else:
            dic[i[1]] += 1
    
    answer = 1
    for v in dic.values():
        answer *= (v + 1)
    
    return answer - 1
