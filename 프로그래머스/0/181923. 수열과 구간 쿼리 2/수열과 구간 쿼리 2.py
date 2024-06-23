def solution(arr, queries):
    answer = []
    
    for slicedArr in queries:
        [s, e, k] = slicedArr

        temp = [x for x in arr[s : e + 1] if x > k] 
        if len(temp) != 0 :
            answer.append(min(temp))
        else : answer.append(-1)
        
    return answer