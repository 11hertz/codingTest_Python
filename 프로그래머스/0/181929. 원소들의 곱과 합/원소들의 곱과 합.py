import math
def solution(num_list):
    return int(sum(num_list) ** 2 > math.prod(num_list))