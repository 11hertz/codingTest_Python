def solution(ineq, eq, n, m):
    answer = 0
    if eq == '!' : eq = ''

    return int(eval(str(n) + ineq + eq + str(m)))