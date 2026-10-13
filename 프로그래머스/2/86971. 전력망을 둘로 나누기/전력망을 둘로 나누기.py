def solution(n, wires):
    graph = [[] for i in range(n+1)]
    
    # 양방향 노드
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
        
    
    def dfs(top, visited):
        cnt = 1 # 본인
        visited[top] = True
        
        for linking in graph[top]:
            if not visited[linking]:
                cnt += dfs(linking, visited)
            
        return cnt
    
    result = n
    
    for wire in wires:
        a = wire[0]
        b = wire[1]
        visited = [False] * (n+1)      # 송전탑 방문 여부
        
        # 전선 끊기
        graph[a].remove(b)
        graph[b].remove(a)

        cnt = dfs(a, visited)
        left_cnt = n - cnt
        
        result = min(result, abs(left_cnt - cnt))
        
        # 전선 복구
        graph[a].append(b)
        graph[b].append(a)

    return result