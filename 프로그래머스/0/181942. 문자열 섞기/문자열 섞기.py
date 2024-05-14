def solution(str1, str2):
    answer = ''
    
    for x in range(len(str1)):
        repeatStr = str1[x] + str2[x]
        answer += repeatStr
    return answer