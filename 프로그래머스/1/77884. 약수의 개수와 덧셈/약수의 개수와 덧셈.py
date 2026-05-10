def solution(left, right):
    answer = 0
    
    def cnt(num):
        num_cnt = 0
        for i in range(1, num+1):
            if num % i == 0:
                num_cnt += 1
                
        return num_cnt 
    
    for i in range(left, right+1):
        if cnt(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    
    return answer