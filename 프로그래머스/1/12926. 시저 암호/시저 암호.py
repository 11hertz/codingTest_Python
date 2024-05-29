def solution(s, n):
    answer = ''
    
    upper = list(range(65, 65 + 26))
    lower = list(range(97, 97 + 26))

    for x in s :
        if x == ' ' : 
            answer += x
            continue
        idx = 0
        if ord(x) in upper : idx = (ord(x) + n) % 65
        elif ord(x) in lower : idx = (ord(x) + n) % 97
    
        if idx >= 26 : idx -= 26
        
        code = 0
        if x.isupper() : code = upper[idx]
        else : code = lower[idx]
        
        answer += chr(code)
    
    return answer