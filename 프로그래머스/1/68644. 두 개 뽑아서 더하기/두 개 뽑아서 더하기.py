from itertools import combinations

def solution(numbers):
    answer = []
    
    total_list = set(combinations(numbers, 2))
    for i in total_list:
        answer.append(sum(i))
    
    set_answer = set(answer)
    
    return sorted(list(set_answer))