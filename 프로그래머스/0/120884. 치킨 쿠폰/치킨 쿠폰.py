def solution(chicken):
    answer = 0;
    coupon = chicken;
    count = 0
    
    while count < len(str(chicken)): 
        answer += int(coupon / 10);
        res = coupon % 10;
        coupon = int(coupon / 10) + res
        count += 1
    
    return answer;