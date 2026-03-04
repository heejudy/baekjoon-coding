def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        if (yellow % i) == 0:
            b = yellow // i 
            if (i >= b):
                if (i + b + 2) == brown // 2:
                    answer = [i + 2, b + 2]    
                
    return answer