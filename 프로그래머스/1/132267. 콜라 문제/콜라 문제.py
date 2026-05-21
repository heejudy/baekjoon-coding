def solution(a, b, n):
    answer = 0
    
    while n >= a: 
        div, mod = (divmod(n, a)) # divmod(20, 3) -> div = 6, mod = 2 

        answer = answer + div * b
        
        n = div * b + mod

    
    print(answer)
    return answer