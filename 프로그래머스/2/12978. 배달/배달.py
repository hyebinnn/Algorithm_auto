import heapq
from collections import defaultdict

def solution(N, road, K):
    INF = float("inf")
    distance = [INF] * (N+1)
    distance[1] = 0  # 시작점 초기화
    info = defaultdict(list)
    
    for row in road:
        a,b,c = row
        info[a].append((b, c))
        info[b].append((a, c))
    
    # (거리, 노드) -> 거리 순으로 최소정렬 될 수 있게끔 거리가 1번째 순서
    heap = [(0, 1)]
    while heap:
        current_dist, current_node = heapq.heappop(heap)

        # remove old data
        if current_dist > distance[current_node]:
            continue
            
        for row in info[current_node]:
            next_node, dist = row
            cost = current_dist + dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))
        
    cnt = 0
    
    for d in distance:
        if d <= K:
            cnt += 1
    
    return cnt