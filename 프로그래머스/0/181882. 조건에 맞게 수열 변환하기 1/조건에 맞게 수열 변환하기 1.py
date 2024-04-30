def solution(arr):
    for x in range(len(arr)):
        if arr[x] % 2 == 0 and arr[x] >= 50:
            arr[x] /= 2
        elif arr[x] % 2 == 1 and arr[x] < 50:
            arr[x] *= 2
    return arr