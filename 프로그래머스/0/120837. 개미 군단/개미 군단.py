def solution(hp):
    gen = hp // 5;
    hp %= 5;
    sol = hp // 3;
    hp %= 3;
    work = hp;
    return gen + sol + work