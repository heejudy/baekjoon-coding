def solution(s):
    answer = True
    
    if len(s) != 4 and len(s) != 6:
        return False
    
    for i in s:
        if ord(i) >= 65 and ord(i) <= 122:
            answer = False
            return answer
        else: 
            answer = True
            
    return answer
    