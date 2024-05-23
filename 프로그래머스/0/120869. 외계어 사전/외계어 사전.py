def solution(spell, dic):
    for x in dic :
        count = 0
        for y in spell :
            if y in x : count += 1
        if count == len(spell) : return 1
    return 2