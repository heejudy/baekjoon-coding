def solution(data, ext, val_ext, sort_by):
    answer = []
    
    a = ["code", "date", "maximum", "remain"]
    what = a.index(ext)
    
    for i in data:
        if i[what] < val_ext: 
            answer.append(i)
    what_sort = a.index(sort_by)
    
    answer.sort(key = lambda x:x[what_sort])
    
    
    return answer