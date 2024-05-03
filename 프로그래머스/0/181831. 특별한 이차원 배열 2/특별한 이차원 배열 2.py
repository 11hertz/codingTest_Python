def solution(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            if(arr[x][y] == arr[y][x]): continue
            else: return 0

    return 1