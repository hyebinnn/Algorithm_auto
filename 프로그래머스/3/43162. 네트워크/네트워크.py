def solution(n, computers):
    visited = [0] * n
    answer = 0

    # 이 컴퓨터는 어느 컴퓨터까지 연결되어있나
    def dfs(num):
        visited[num] = 1
        for j in range(len(computers[0])):
            if num == j:
                continue
                
            # i,j가 연결되어있고 연결된 j 컴퓨터에 방문하지 않은 경우
            if not visited[j] and computers[num][j] == 1:
                dfs(j)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
        
    return answer