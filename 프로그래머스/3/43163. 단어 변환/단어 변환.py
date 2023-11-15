# from collections import deque

def solution(begin, target, words):
    res = []
    visited = []
    if target not in words:
        return 0
    def dfs(current, cnt):
        visited.append(current)
        for w in words:
            diff = 0
            for j in range(len(current)):
                if w[j] != current[j]:
                    diff += 1
            if diff == 1 and w not in visited:
                if w == target:
                    res.append(cnt+1)
                    return
                dfs(w, cnt+1)
                
    
    dfs(begin, 0)
    
    return min(res)
                
        
    
    
#### BFS
# =========================
#     queue = deque()
#     queue.append((begin, 0))
#     d = dict()
#     visited = dict()
#     for x in words:
#         d[x] = int(1e6)
#         visited[x] = 0
#     if target not in words:
#         return 0
#     def getSimilarWord(current, cnt):
#         for w in words:
#             diff = 0
#             for j in range(len(current)):
#                 if w[j] != current[j]:
#                     diff += 1
#             if diff == 1 and not visited[w]:
#                 d[w] = min(d[w], cnt+1)
#                 queue.append((w, cnt+1))
                
#     cnt = 0
#     while queue:
#         word, cnt = queue.popleft()
#         visited[word] = 1
#         getSimilarWord(word, cnt)
                          
#     return d[target]
        