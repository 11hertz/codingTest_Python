def solution(numbers):
    arr = []
    
    for x in range(len(numbers) - 1):
        for y in range(len(numbers)):
            if x == y : continue
            else : 
                num = numbers[x] + numbers[y]
                arr.append(num)

    return sorted(list(set(arr)))