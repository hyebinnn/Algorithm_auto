from collections import deque

def solution(priorities, location):
    queue = deque([(i, priorities[i]) for i in range(len(priorities))])
    cnt = 0
    
    while queue:
        x = queue.popleft()
        if any(x[1] < pri for idx, pri in queue):
            queue.append(x)
            continue
        cnt += 1
        if x[0] == location:
            return cnt
        
        
        
        
#         for i in range(len(priorities)):
#             if priorities[i] > priorities[x]:
#                 queue.append(x)
#                 break
            
        