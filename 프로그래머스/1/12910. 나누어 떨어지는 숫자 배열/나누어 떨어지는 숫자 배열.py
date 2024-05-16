def solution(arr, divisor):
    answer = sorted([x for x in arr if x % divisor == 0])
    return [-1] if len(answer) < 1 else answer