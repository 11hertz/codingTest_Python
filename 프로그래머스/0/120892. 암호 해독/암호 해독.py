def solution(cipher, code):
    return ''.join(cipher[x - 1] for x in range(1, len(cipher) + 1) if x % code == 0)