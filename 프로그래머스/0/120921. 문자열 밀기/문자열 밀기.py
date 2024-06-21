def solution(A, B):
    answer = 0
    
    for x in range(len(A)):
        if A == B : return answer
        B = B[1:] + B[:1] 
        answer += 1
    
    return answer if answer < len(A) else -1