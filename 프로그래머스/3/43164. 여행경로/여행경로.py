def solution(tickets):
    result = []
    def getRoute(end):
        nonlocal temp
        for i in range(len(tickets)):
            if tickets[i][0] == end and not visited[i]:
                temp.append(tickets[i][0])
                visited[i] = 1
                getRoute(tickets[i][1])
                visited[i] = 0
                temp.pop()              # for 백트래킹
                
            elif tickets[i][0] != end and i == len(tickets) - 1 and 0 not in visited:
                temp.append(end)
                temp2 = temp.copy()
                result.append(temp2)
                temp.pop()                  # 모든 항공권 사용 후 마지막 도착 도시 제거 (for 백트래킹) 
                    
    
    for i in range(len(tickets)):
        visited = [0] * len(tickets)
        if tickets[i][0] == "ICN":
            temp = ["ICN"]
            visited[i] = 1
            getRoute(tickets[i][1])
            
    result.sort()
    return result[0]