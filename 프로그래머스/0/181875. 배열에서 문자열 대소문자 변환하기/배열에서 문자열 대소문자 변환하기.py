def solution(strArr):
    return [strArr[x].lower() if x % 2 == 0 else strArr[x].upper() for x in range(len(strArr))]