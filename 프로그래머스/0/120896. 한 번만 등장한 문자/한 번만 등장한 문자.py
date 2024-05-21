def solution(s):
    strList = sorted(list(s)) 
    return ''.join(x for x in strList if strList.count(x) == 1)