def solution(n, s):
    answer = []
    remainder = 0
    
    if (n <= s):
        answer = [s//n for i in range(n)]
        remainder = s - (s//n * n)
        for i in range(remainder):
            answer[i] += 1
            
            
    else: 
        answer = [-1]

    
    return sorted(answer)