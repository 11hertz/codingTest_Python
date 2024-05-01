def solution(age):
    alpha = 'abcdefghijklmnopqrstuvwxyz' 
    return ''.join(alpha[int(x)] for x in str(age))