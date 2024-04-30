def solution(todo_list, finished):
    return [todo_list[x] for x in range(len(finished)) if not finished[x]]