def solution(s):
    numArr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for idx in range(len(numArr)):
        s = s.replace(numArr[idx], str(idx))
        
    return int(s)