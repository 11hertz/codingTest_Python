def solution(a, d, included):
    arr = []
    for x in range(a, a + len(included) * d, d) :
        arr.append(x)

    return sum(arr[x] for x in range(len(arr)) if included[x] == True)