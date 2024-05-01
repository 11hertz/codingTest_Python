def solution(num_list):
    oddSum = ''
    evenSum = ''
    
    for x in range(len(num_list)):
        if num_list[x] % 2:
            oddSum += str(num_list[x])
        else:
            evenSum += str(num_list[x])
            
    return int(oddSum) + int(evenSum)