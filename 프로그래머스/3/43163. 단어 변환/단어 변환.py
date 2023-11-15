from collections import deque

def solution(begin, target, words):
    queue = deque()
    queue.append((begin, 0))
    d = dict()
    visited = dict()
    for x in words:
        d[x] = int(1e6)
        visited[x] = 0
    if target not in words:
        return 0
    def getSimilarWord(current, cnt):
        for w in words:
            diff = 0
            for j in range(len(current)):
                if w[j] != current[j]:
                    diff += 1
            if diff == 1 and not visited[w]:
                d[w] = min(d[w], cnt+1)
                queue.append((w, cnt+1))
                
    cnt = 0
    while queue:
        word, cnt = queue.popleft()
        visited[word] = 1
        getSimilarWord(word, cnt)
                          
    return d[target]
        