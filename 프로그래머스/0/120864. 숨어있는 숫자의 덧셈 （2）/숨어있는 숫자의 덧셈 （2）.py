import re
def solution(my_string):
    text = re.sub('([A-z])', ' ', my_string).split()
    return sum(list(map(int, text)))