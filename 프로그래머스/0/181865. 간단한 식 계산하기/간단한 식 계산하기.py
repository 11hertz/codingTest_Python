def solution(binomial):
    def calculation(txt):
        a, op, b = txt.split(' ')
        if(op == '+') : return int(a) + int(b)
        elif(op == '-') : return int(a) - int(b)
        else : return int(a) * int(b)
    return calculation(binomial)