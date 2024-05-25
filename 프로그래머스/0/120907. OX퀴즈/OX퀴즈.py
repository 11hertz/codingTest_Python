def solution(quiz):
    answer = []
    
    for q in quiz :
        formula, res = q.split('=')
        if eval(formula) == int(res) : answer.append('O')
        else : answer.append('X')

    return answer