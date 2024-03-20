n=int(input())
t=[]
p=[]
dp=[]
for i in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(n-1,-1,-1):
    if t[i]+i > n:
        dp[i]=dp[i+1]   # 0으로
    else:
        dp[i]=max(p[i]+dp[i+t[i]], dp[i+1])
print(dp[0])