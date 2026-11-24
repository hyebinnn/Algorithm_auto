from collections import defaultdict

def solution(n, computers):
    link = defaultdict(list)
    visited = [False] * n
    
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if i == j:
                continue
            
            if computers[i][j] == 1:
                link[i].append(j)
        
        
    def dfs(computer):
        visited[computer] = True

        for value in link[computer]:
            if not visited[value]:
                dfs(value)
        
    
    # computer iteration
    network = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            network += 1
        
    
    return network