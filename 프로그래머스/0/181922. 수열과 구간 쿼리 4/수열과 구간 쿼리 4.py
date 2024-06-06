def solution(arr, queries):
    for x in queries:
        s, e, k = x
        for y in range(s, e + 1):
            if y % k == 0 : arr[y] += 1
    
    return arr