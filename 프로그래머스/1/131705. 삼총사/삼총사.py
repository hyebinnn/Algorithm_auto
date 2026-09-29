def solution(number):
    N = len(number)
    result = []
    
    def get_answer(start):
        if len(result) == 3:
            if sum(result) == 0:
                return 1
            else: 
                return 0
    
        cnt = 0
            
        for i in range(start, N):
            result.append(number[i])
            cnt += get_answer(i+1)
            result.pop()
        
        return cnt
        
    return get_answer(0)