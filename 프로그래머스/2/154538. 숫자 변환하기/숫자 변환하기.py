from collections import deque

def solution(x, y, n):
    queue = deque([(x, 0)])
    visited = {x}
    
    while queue:
        x, cnt = queue.popleft()
        
        if x == y:
                return cnt
            
        next_values = [
            x+n, x*2, x*3
        ]
        
        for nv in next_values:
            if nv in visited:
                continue
            if nv > y:
                continue
            visited.add(nv)
            queue.append((nv, cnt+1))
            
    return -1