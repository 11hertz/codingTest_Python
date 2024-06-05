def solution(sizes):
    arr1 = []
    arr2 = []
    for x in sizes:
        a, b = sorted(x)
        arr1.append(a)
        arr2.append(b)

    return max(arr1) * max(arr2)