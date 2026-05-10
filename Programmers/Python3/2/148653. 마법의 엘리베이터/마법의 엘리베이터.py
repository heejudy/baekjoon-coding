def solution(storey):
    answer = 0
    
    while storey > 0:
        num = storey % 10 
        
        if num < 5:
            answer += num
            storey //= 10
        
        elif num > 5:
            answer += (10 - num)
            storey = storey // 10 + 1
        
        else:  
            next_num = (storey // 10) % 10
            
            if next_num >= 5:
                answer += 5
                storey = storey // 10 + 1
            else:
                answer += 5
                storey //= 10
    
    return answer