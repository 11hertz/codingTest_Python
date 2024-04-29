def solution(array, height):
    return sum(True for student in array if student > height)