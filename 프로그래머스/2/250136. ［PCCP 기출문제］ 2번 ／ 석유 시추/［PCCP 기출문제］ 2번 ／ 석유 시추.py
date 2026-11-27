from collections import deque

def solution(land):
    N, M = len(land), len(land[0])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    answer = 0
    oil_id = 2
    size = {}
    
    # 덩어리 크기 리턴
    def bfs():
        cnt = 1
        while queue:
            x, y = queue.popleft()
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0<=nx<N and 0<=ny<M and land[nx][ny] == 1:
                    land[nx][ny] = oil_id
                    queue.append((nx, ny))
                    cnt += 1

        return cnt
    
    
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1:
                land[i][j] = oil_id
                queue.append((i, j))
                size[oil_id] = bfs()
                oil_id += 1
                
    # i = 시추기 열 위치
    for i in range(M):
        result = 0
        visited = []
        for j in range(N):
            num = land[j][i]
            if num != 0 and num not in visited:
                result += size[num]
                visited.append(num)
                
        answer = max(result, answer)
        
    return answer