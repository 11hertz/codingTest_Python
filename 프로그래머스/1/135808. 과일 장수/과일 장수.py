def solution(k, m, score):
    answer = 0
    
    score.sort(reverse = True)
    
    for x in range(0, len(score), m):
        if len(score[x : x + m]) == m :
            answer += min(score[x : x + m]) * len(score[x : x + m])
        
    return answer