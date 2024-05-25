def solution(quiz):
    answer = []
    
    for q in quiz :
        num1, oper1, num2, eq, res = q.split(' ')
        if eval(num1 + oper1 + num2) == int(res) : answer.append('O')
        else : answer.append('X')
    
    return answer