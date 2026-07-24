from collections import Counter

def solution(participant, completion):
    a = Counter(participant)
    b = Counter(completion)
    
    return next(iter(a-b))
    
    
    
    
    
    
    
    
    # participant.sort()
    # completion.sort()
    # for i in range(len(completion)):
    #     if participant[i] != completion[i]:
    #         return participant[i]
    # return participant[-1]