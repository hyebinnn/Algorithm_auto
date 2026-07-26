from collections import deque

def solution(board):
    # 가로 N, 세로 M
    global N, M 
    N, M = len(board[0]), len(board)
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    # 멈춘 위치만 방문 저장
    visited = [[-1] * N for _ in range(M)]
    queue = deque()
    
    # 시작점
    for i in range(M):
        for j in range(N):
            if board[i][j] == "R":
                queue.append((i, j, 0))
                visited[i][j] = 1
    
    while queue:
        x, y, cnt = queue.popleft()
            
        for dx, dy in direction:
            # 지금 방향대로 slip() 미끄러지기
            stop_x, stop_y = slip(x, y, dx, dy, board)
            if stop_x == x and stop_y == y:
                continue
            if visited[stop_x][stop_y] == 1:
                continue
                
            # 미끄러지면서 이동
            print((stop_x, stop_y, cnt+1))
            
            if board[stop_x][stop_y] == "G":
                return cnt+1
            
            queue.append((stop_x, stop_y, cnt+1))
            visited[stop_x][stop_y] = 1
               
    return -1
               

def slip(x, y, dx, dy, board):
    while True:
        nx, ny = x+dx, y+dy
        if not (0 <= nx < M and 0 <= ny < N):
               break
        if board[nx][ny] == "D":
               break
        x, y = nx, ny

    return (x, y)