from collections import deque

def oilGroup(i, j, land, groupNumber, n, m, visited):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque()
    queue.append((i, j))
    visited[i][j] = groupNumber             # 방문 확인하면 해당 그룹 넘버로 저장
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+d[i][0], y+d[i][1]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and land[nx][ny] == 1:
                visited[nx][ny] = groupNumber
                queue.append((nx, ny))
                count += 1
    
    return count
    
    
    

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[0]*m for _ in range(n)]
    groupNum = 1
    group = [0]
    
    # 석유땅 그룹화
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                count = oilGroup(i, j, land, groupNum, n, m, visited)
                group.append(count)         # group 별 석유량 (group은 1번부터 유효한 수)
                groupNum += 1
                
    res = []
    for r in range(m):
        oil = set()
        amount = 0
        for c in range(n):
            if land[c][r] == 1:
                oil.add(visited[c][r])
        for g in oil:
            amount += group[g]
        res.append(amount)
    
    # print(res)
    return max(res)