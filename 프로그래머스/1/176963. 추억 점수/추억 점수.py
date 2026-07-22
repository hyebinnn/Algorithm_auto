def solution(name, yearning, photo):
    answer = []
    
    score = dict(zip(name, yearning))
    # for i in range(len(name)):
    #     m[name[i]] = yearning[i]
    
    for people in photo:
        total = 0
        for p in people:
            if p in score:
                total += score.get(p, 0)
        
        answer.append(total)
                
    
    return answer