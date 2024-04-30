def solution(names):
    return [names[x] for x in range(len(names)) if x % 5 == 0]