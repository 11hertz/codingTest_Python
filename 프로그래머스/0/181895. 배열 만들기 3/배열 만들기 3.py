def solution(arr, intervals):
    S1, E1 = intervals[0]
    S2, E2 = intervals[1]
    return arr[S1 : E1 + 1] + arr[S2 : E2 + 1]