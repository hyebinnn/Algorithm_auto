def rotation(spell, d):
    for s in spell:
        if s not in d:
            return -1
    return 1
        

def solution(spell, dic):
    for s in spell:
        for d in dic:
            if s in d:
                if rotation(spell, d) == 1:
                    return 1
        return 2
    