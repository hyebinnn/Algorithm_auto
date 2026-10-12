def solution(k, dungeons):
    visited = [False] * len(dungeons)

    def dfs(energy):
        best = 0

        for i in range(len(dungeons)):
            required, cost = dungeons[i]

            # 이미 방문했거나 입장할 피로도가 부족하면 건너뛰기
            if visited[i] or energy < required:
                continue

            visited[i] = True
            candidate = 1 + dfs(energy - cost)
            best = max(best, candidate)
            visited[i] = False

        return best

    return dfs(k)