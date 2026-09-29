def solution(number):
    N = len(number)
    result = []
    cnt = 0
    
    def get_answer(start):
        nonlocal cnt
        if len(result) == 3:
            if sum(result) == 0:
                cnt += 1
            return
            
        for i in range(start, N):
            result.append(number[i])
            get_answer(i+1)
            result.pop()
        
    get_answer(0)
    return cnt