def solution(myString, pat):
    answer = []
    for x in myString:
        if(x == 'A') : answer.append('B')
        else : answer.append('A')
    return 1 if ''.join(answer).find(pat) >= 0 else 0