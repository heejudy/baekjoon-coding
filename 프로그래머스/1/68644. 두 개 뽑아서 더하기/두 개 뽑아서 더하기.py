from itertools import combinations

def solution(numbers):
    answer = []
    
    total_list = set(combinations(numbers, 2))
    for i in total_list:
        answer.append(sum(i))
    
    set_answer = set(answer)
    set_same = set()
    
    for i in numbers:
        set_same.add(i*2)
        
    minus_set = set_same - set_answer
    
    return sorted(list(set_answer - minus_set))