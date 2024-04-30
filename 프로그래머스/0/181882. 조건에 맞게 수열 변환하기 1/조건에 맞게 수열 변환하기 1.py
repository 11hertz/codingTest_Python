def solution(arr):
    for x in range(len(arr)):
        if arr[x] >= 50 and not arr[x] % 2:
            arr[x] //= 2
        elif arr[x] < 50 and arr[x] % 2:
            arr[x] *= 2
    return arr