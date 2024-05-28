def solution(array, n):
    array.sort()
    dis_array = [abs(x - n) for x in array]
    idx = dis_array.index(min(dis_array))
    
    return array[idx]