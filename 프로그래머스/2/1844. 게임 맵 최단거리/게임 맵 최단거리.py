from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    INF = float("inf")
    
    queue = deque([(0, 0)])
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and maps[nx][ny] and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            
    if visited[N-1][M-1] == 0:
        return -1
    else:
        return visited[N-1][M-1]
    
    
    