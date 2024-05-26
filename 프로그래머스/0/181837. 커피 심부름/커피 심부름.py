def solution(order):
    return sum(5000 if 'cafelatte' in coffee else 4500 for coffee in order)