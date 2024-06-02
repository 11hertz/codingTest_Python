def solution(strArr):
    arr = [len(x) for x in strArr]
    setArr = list(set(arr))
    
    return max(arr.count(x) for x in setArr)