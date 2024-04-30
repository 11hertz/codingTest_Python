def solution(todo_list, finished):
    answer = [todo_list[x] for x in range(len(finished)) if not finished[x]]
    return answer