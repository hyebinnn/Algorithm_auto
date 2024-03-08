# # 유기농 배추
# dfs
import sys
sys.setrecursionlimit(10000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    garden = [[0]*m for _ in range(n)]
    location = set()   
    for _ in range(k):
        x, y = map(int, input().split())
        garden[y][x] = 1
        location.add((x, y))
       
    count = 0
    
    def dfs(idx):
        x, y = idx
        garden[y][x] = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and garden[ny][nx] == 1:
                dfs((nx, ny))

    for x, y in location:
        if garden[y][x]:
            dfs((x, y))
            count += 1
    
    print(count)        