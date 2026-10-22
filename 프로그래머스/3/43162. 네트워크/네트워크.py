def solution(n, computers):
    visited = [False] * n
    
    def dfs(idx):
        visited[idx] = 1
        
        for k in range(n):
            if k == idx:
                continue
            if computers[idx][k] == 1 and not visited[k]:
                dfs(k)

    cnt = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt += 1
            
        
    return cnt