def solution(s):
    answer = []
    index_dic = {}
    
    for i in range(len(s)):
        if s[i] not in index_dic:
            index_dic[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - index_dic[s[i]])
            index_dic[s[i]] = i
            
    return answer