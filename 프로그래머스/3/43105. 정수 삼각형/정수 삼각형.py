def solution(triangle):
    n = len(triangle)
    direction = [(-1, -1), (-1, 0)]
    dp = [[0] * x for x in range(1, n+1)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(i+1):
            for x, y in direction:
                nx, ny = i+x, j+y
                if 0<=nx<n and 0<=ny<i:
                    dp[i][j] = max(triangle[i][j]+dp[nx][ny], dp[i][j])
    
    return max(dp[n-1])
                
            