def solution(arr):
    answer = arr
    
    for x in range(0, 11):
        target = 2 ** x
        if len(arr) == target : break
        if target > len(arr) :
            for _ in range(target - len(arr)) : 
                arr.append(0)
            break
    
    return answer