def solution(order):
    return sum(4500 if 'americano' in coffee or 'anything' in coffee else 5000 for coffee in order)