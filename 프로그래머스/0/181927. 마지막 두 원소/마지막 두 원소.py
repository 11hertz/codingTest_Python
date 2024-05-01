def solution(n_list):
    n_list.append(n_list[-1] - n_list[-2] if n_list[-1] > n_list[-2] else n_list[-1] * 2)
    return n_list