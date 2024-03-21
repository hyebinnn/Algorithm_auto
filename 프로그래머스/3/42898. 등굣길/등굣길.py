def solution(m, n, puddles):
    board = [[0] * (m) for _ in range(n)]
    d = [(0, -1), (-1, 0)]
    board[0][0] = 1
    
    # water pool
    for x, y in puddles:
        board[y-1][x-1] = -1
                    
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:
                continue
            for x, y in d:
                nx, ny = i+x, j+y
                if nx >= 0 and ny >= 0 and board[nx][ny] != -1:   # 왼쪽 위쪽 하나씩 확인
                    board[i][j] += board[nx][ny]
        
    return board[n-1][m-1] % 1000000007