def solution(arr):
    fIdx = -1
    lIdx = -1
    
    for idx, x in enumerate(arr):
        if x == 2 and fIdx == -1 : fIdx = idx
        elif x == 2 and fIdx != -1 : lIdx = idx
    
    if fIdx != -1 and lIdx != -1 : return arr[fIdx : lIdx + 1]
    elif fIdx != -1 and lIdx == -1 : return [arr[fIdx]]
    
    return [-1]