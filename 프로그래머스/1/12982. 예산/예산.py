def solution(d, budget):
    d.sort()
    
    total = 0
    count = 0
    for x in range(len(d)):
        total += d[count]
        if total > budget : break
        count += 1

    return count