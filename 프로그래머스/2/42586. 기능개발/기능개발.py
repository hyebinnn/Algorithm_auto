from collections import deque

def solution(progresses, speeds):
    queue = deque(enumerate(progresses))
    cnt = 0
    result = []
    
    while queue:
        idx, progress = queue.popleft()
            
        if progress >= 100:
            cnt += 1
            continue
            
        if cnt > 0: 
            result.append(cnt)
            cnt = 0
            
        queue.appendleft((idx, progress))
        
        for pos in range(len(queue)):
            i, progress = queue[pos]
            queue[pos] = (i, progress+speeds[i])
        
    if cnt > 0:
        result.append(cnt)
        
    return result