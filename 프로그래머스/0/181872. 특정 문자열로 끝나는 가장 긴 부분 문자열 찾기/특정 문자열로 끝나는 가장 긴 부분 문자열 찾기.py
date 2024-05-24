def solution(myString, pat):
    lastIdx = max(x for x in range(len(myString) + 1) if myString.endswith(pat, 0, x))
    return myString[0 : lastIdx]