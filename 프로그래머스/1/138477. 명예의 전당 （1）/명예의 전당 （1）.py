def solution(k, score):
    answer = []
    HOF = []
    
    for x in score:
        if len(HOF) < k : HOF.append(x)
        else : 
            if x > min(HOF) : 
                HOF.remove(min(HOF))
                HOF.append(x)
        answer.append(min(HOF))

    return answer