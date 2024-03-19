# 숨바꼭질 3

import heapq

n, k = map(int, input().split())
q = []
heapq.heappush(q, (0, n))
dist = [1e6] * 100001
dist[n] = 0

while q:
    d, start = heapq.heappop(q)
    for nx in [(1, start+1), (1, start-1), (0, start*2)]:
        if 0 <= nx[1] <= 100000 and dist[nx[1]] > d + nx[0]:
            # 현재에서 이동한게 더 최솟값이라면 갱신
            dist[nx[1]] = d + nx[0]
            heapq.heappush(q, (dist[nx[1]], nx[1]))
    
print(dist[k])





















