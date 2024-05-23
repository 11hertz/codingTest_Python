def solution(s):
    strList = list(s)
    strList.sort(reverse=True)
    
    return ''.join(strList)