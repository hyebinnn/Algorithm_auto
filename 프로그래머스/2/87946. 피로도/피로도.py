def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = 0
    
    def dfs(health, count):
        nonlocal answer
        answer = max(count, answer)
        
        for i in range(len(dungeons)):
            need, consume = dungeons[i]
            
            # 탐험 가능
            if not visited[i] and health >= need:
                visited[i] = True
                dfs(health-consume, count + 1)
                visited[i] = False
                    
    dfs(k, 0)
    return answer