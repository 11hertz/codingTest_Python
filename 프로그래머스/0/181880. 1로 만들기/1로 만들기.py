def solution(num_list):
    def makeOne(num):
        count = 0
        while num > 1:
            if num % 2 == 0 : num /= 2
            else : num = (num - 1) / 2
            count += 1
        return count

    return sum(makeOne(x) for x in num_list)