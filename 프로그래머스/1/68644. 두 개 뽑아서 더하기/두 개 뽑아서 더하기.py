def solution(numbers):
    arr = []
    
    for x in range(len(numbers) - 1):
        for y in range(x + 1, len(numbers)):
            arr.append(numbers[x] + numbers[y])

    return sorted(list(set(arr)))