def solution(polynomial):
    xTerm = 0
    numTerm = 0
    
    for term in polynomial.split(' + '):
        if 'x' in term and len(term) > 1:
            xTerm += int(term[:len(term) - 1])
        elif 'x' in term and len(term) == 1:
            xTerm += 1
        else :
            numTerm += int(term)
        
    if xTerm > 1 and numTerm > 0 : return str(xTerm) + 'x + ' + str(numTerm)
    elif xTerm > 1 and numTerm == 0 : return str(xTerm) + 'x'
    elif xTerm == 1 and numTerm != 0 : return 'x + ' + str(numTerm)
    elif xTerm == 0 and numTerm != 0 : return str(numTerm)
    elif xTerm == 1 and numTerm == 0 : return 'x'
    