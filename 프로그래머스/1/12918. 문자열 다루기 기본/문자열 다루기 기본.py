import re
def solution(s):
    repalcedStr = re.sub('\d', '', s)
    return (len(s) == 4 or len(s) == 6) and len(repalcedStr) == 0