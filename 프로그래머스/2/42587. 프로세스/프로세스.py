from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))
    cnt = 0
    
    while queue:
        idx, priority = queue.popleft()
        
        for ni, np in queue:
            if np > priority:
                queue.append((idx, priority))
                break
        else:
            cnt += 1
            
            if idx == location:
                return cnt
                
    
    
    