def solution(s, n):
    answer = ''

    n %= 26

    for i in s:
        if i == ' ':
            answer += ' '

        elif 'A' <= i <= 'Z':
            # ord(i) - ord('A') => 'A'를 기준점(0)으로 만듦 
            # + n => 이동 
            # % 26 => 반복하는 경우 ('Z'를 넘는 경우)
            # + ord('A') => 아스키문자 영역으로 변경 
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))

        else:
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))

    return answer

# A -> 65 
# Z -> 90
# a -> 97
# z -> 122 
