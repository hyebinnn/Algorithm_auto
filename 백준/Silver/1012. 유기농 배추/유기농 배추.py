import sys
sys.setrecursionlimit(10000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    garden = [[0]*m for _ in range(n)]    
    sx, sy = map(int, input().split())
    garden[sy][sx] = 1
    for _ in range(k-1):
        x, y = map(int, input().split())
        garden[y][x] = 1
        
    def getIdxOne(board):
        for i in range(len(board)):
            if 1 in board[i]:
                j = board[i].index(1)
                return (j, i)
        return -1

    count = 0
    
    def dfs(idx):
        x, y = idx
        garden[y][x] = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and garden[ny][nx] == 1:
                dfs((nx, ny))

    dfs((sx, sy))
    count += 1   
    res = getIdxOne(garden)

    while res != -1:
        dfs(res)
        count += 1
        res = getIdxOne(garden)
    
    print(count)        