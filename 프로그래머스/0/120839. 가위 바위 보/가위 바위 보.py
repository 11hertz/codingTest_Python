def solution(rsp):
    cases = { '0':'5', '2':'0', '5':'2' }
    return ''.join(cases[x] for x in rsp)