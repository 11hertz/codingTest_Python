def solution(answers):
    answer = []
    
    p1 = [1, 2, 3, 4, 5];
    p2 = [2, 1, 2, 3, 2, 4, 2, 5];
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    score = [0, 0, 0]
    
    for x in range(len(answers)):
        if p1[x % len(p1)] == answers[x] : score[0] += 1  
        if p2[x % len(p2)] == answers[x] : score[1] += 1   
        if p3[x % len(p3)] == answers[x] : score[2] += 1
    
    
    maxScore = max(score);
    
    for i, x in enumerate(score):
        if x == maxScore : answer.append(i + 1)
    
    
    return answer