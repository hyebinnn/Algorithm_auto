from collections import deque
from pprint import pprint

def solution(maps):
    N = len(maps[0])  # 가로 = y 
    M = len(maps)     # 세로 = x
    INF = float('inf')
    visited = [[False] * N for _ in range(M)]
    board = [[INF] * N for _ in range(M)]
    board[0][0] = 1
    visited[0][0] = True
    queue = deque([(0,0)])
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    while queue:
        x, y = queue.popleft()
        
        for d in direction:
            nx, ny = x + d[0], y + d[1]
            if not (0<=nx<M and 0<=ny<N) or maps[nx][ny] == 0:
                continue
                
            board[nx][ny] = min(board[nx][ny], board[x][y] + 1)
            
            if not visited[nx][ny]:
                # 다음으로 이동할 좌표
                queue.append((nx, ny))
                visited[nx][ny] = True
                
    
    return board[M-1][N-1] if board[M-1][N-1] != INF else -1

