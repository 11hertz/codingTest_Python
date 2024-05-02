def solution(my_string, num1, num2):
    swapStr = list(my_string)
    swapStr[num1], swapStr[num2] = swapStr[num2], swapStr[num1]
    return ''.join(swapStr)