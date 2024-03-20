n, k = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(n)]           # weight, value
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w = things[i-1][0]
    v = things[i-1][1]
    for j in range(1, k+1):
        # 가방에 넣을 수 있다면
        if j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]
            
            
print(dp[n][k])