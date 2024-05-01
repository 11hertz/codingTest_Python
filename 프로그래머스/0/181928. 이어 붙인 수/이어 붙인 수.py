def solution(num_list):
    oddSum = ''.join(str(num_list[x]) for x in range(len(num_list)) if num_list[x] % 2)
    evenSum = ''.join(str(num_list[x]) for x in range(len(num_list)) if not num_list[x] % 2)
    return int(oddSum) + int(evenSum)