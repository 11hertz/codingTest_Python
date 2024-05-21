def solution(myString, pat):
    return sum(1 for x in range(len(myString) - len(pat) + 1) if myString[x : x + len(pat)] == pat)