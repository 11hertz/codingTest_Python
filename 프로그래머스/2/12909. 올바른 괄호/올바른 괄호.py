def solution(s):
    answer = True
    stack = []
    for x in s:
        if x == '(' : stack.append(x)
        elif len(stack) > 0 : stack.pop()
        else : return False
    
    return True if len(stack) == 0 else False