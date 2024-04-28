def solution(numbers):
    def double(x):
        return x * 2;
    return list(map(double, numbers))