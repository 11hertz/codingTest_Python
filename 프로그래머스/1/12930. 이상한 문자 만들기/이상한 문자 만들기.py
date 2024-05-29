def solution(s):
    answer = ''
    
    count = 0
    for x in s :
        if x == ' ' :
            count = 0
            answer += ' '
            continue
        if count % 2 == 0 : answer += x.upper()
        else : answer += x.lower()
        count += 1
        
    return answer