from functools import reduce
def solution(box, n):
    answer = reduce(lambda acc, cur: acc * (cur // n), box, 1)
    return answer