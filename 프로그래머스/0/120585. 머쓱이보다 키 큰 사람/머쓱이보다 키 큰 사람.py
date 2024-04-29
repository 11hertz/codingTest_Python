def solution(array, height):
    return sum([student > height for student in array])