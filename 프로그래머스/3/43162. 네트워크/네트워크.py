from collections import defaultdict

def solution(n, computers):
    link = defaultdict(list)
    visited = [0] * n
    answer = 0
    
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if i == j:
                continue
            if computers[i][j] == 1:
                link[i].append(j)
    
    # 이 컴퓨터는 어느 컴퓨터까지 연결되어있나
    def dfs(num):
        visited[num] = 1
        for com in link[num]:
            if not visited[com]:
                dfs(com)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
        
    return answer