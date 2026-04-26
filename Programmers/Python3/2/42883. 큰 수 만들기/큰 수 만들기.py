# def solution(number, k):
#     answer = ''
    
#     lst = list(i for i in number)
#     lst_sort = sorted(lst)[0:k]
    
#     for i in lst_sort:
#         lst.remove(i)
    
#     for i in lst:
#         answer += i
#     return answer
# 이상함 


def solution(number, k):
    st = []
    
    for i in number:
        while st and k > 0 and st[-1] < i:
            st.pop()
            k -= 1
        st.append(i)
    
    if k > 0:
        st = st[:-k]
    
    return ''.join(st)