def solution(name, yearning, photo):
    answer = []
    
    m = dict()
    
    for i in range(len(name)):
        m[name[i]] = yearning[i]
    
    for i in range(len(photo)):
        result = 0
        for j in range(len(photo[i])):
            p = photo[i][j]
            
            if p in m.keys():
                result += m[p]
        
        answer.append(result)
                
    
    return answer