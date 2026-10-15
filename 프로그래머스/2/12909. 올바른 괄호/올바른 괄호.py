from collections import deque

def solution(s):
    queue = deque()
    
    for value in s:
        if value == ")":
            if not queue:
                return False
            else:
                queue.popleft()
                continue
        else:
            queue.append(value)
            
    return False if queue else True