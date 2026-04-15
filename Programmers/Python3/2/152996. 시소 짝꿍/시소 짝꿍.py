def solution(weights):
    answer = 0
    dic = dict()
    
    weights.sort()
    
    for w in weights:
        for i in [1, 2/3, 1/2, 3/4]:
            f = w * i
            answer += dic.get(f, 0)
        
        dic[w] = dic.get(w, 0) + 1
    
    return answer