def solution(numbers):
    numArr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for idx, text in enumerate(numArr):
        numbers = numbers.replace(numArr[idx], str(idx))
    
    return int(numbers)