from collections import deque

def solution(progresses, speeds):
    queue = deque(zip(progresses, speeds))
    result = []
    
    while queue:
        cnt = 0
        
        # 작업 
        for i in range(len(queue)):
            p, s = queue[i]
            queue[i] = (p+s, s)
        
        while queue and queue[0][0] >= 100:
            cnt += 1
            queue.popleft()
            
        if cnt != 0:
            result.append(cnt)
        
    return result