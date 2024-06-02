def solution(picture, k):
    answer = []
    
    for x in picture:
        str = ''
        for y in x:
            str += y * k
        
        for z in range(k) : answer.append(str)

    return answer