def solution(common):
    A, B, C = common[0 : 3]
    
    if B - A == C - B : return common[-1] + (B - A)
    else : return common[-1] * (B // A)
