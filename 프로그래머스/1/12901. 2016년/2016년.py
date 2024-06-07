def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    
    month = sum(days[:a - 1])
    
    return date[(month + b) % 7]