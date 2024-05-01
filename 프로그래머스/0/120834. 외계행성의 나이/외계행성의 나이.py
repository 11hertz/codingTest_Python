def solution(age):
    alpha = 'abcdefghij' 
    return ''.join(alpha[int(x)] for x in str(age))