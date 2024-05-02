def solution(arr, intervals):
    answer = []
    for x in range(len(intervals)):
        answer += arr[intervals[x][0] : intervals[x][1] + 1]
    return answer