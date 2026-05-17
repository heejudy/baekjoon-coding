def solution(n):
    answer = 0
    
    def change(num, q):
        result = ''
        
        while num > 0:
            num, mod = divmod(num, q)
            result += (str(mod))
        
        return result
    
    tothree = change(n, 3)
    answer = int(tothree, 3)
    
    
    return answer