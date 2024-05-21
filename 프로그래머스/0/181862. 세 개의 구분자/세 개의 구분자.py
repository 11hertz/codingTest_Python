import re
def solution(myStr):
    text = re.sub('(a|b|c)', ' ', myStr)
    return text.lstrip().split() or ['EMPTY']