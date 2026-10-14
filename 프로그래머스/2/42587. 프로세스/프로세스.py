from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))
    cnt = 0
    
    while queue:
        idx, priority = queue.popleft()
        
        if any(p > priority for _, p in queue):
            queue.append((idx, priority))
        else:
            cnt += 1
            
            if idx == location:
                return cnt
                
    
    
    