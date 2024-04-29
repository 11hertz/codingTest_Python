def solution(my_string):
    return sum(int(x) for x in my_string if (x in '123456789'))