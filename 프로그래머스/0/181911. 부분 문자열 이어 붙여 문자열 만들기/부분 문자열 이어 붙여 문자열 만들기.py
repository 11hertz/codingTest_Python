def solution(my_strings, parts):
    return ''.join(my_strings[x][parts[x][0]:parts[x][1] + 1] for x, y in enumerate(parts))