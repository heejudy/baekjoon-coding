def solution(strings, n):
    answer = []
    dic = {}
    
    for i in strings:
        if i[n] not in dic:
            dic[i[n]] = [i]
        else:
            dic[i[n]].append(i)

    print(dic)
    # sorted_dic = dict(sorted(dic.items(), key=lambda x: x[1]))
    sorted_dic = dict(sorted(dic.items()))
    
    print(sorted_dic)
    
    for i in list(sorted_dic.values()):
        answer.extend(sorted(i))
    return answer