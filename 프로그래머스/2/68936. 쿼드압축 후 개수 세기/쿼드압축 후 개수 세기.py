def solution(arr):
    answer = [0, 0]   # [0의 개수, 1의 개수]

    def quad(x, y, size):
        first = arr[x][y]
        same = True
        # TODO 1: 영역 안 모든 칸이 first와 같은지 확인
        #         같으면 answer[first] += 1 하고 return
        for i in range(x, x+size):
            for j in range(y, y+size):
                if arr[i][j] != first:
                    same = False
                    break
            if not same:
                break
        else:
            # 압축 성공
            answer[first] += 1
            return

        # 압축 실패
        half = size // 2
        
        # 4등분한 윈쪽 상단 시작좌표 재귀
        quad(x, y, half)
        quad(x, y+half, half)
        quad(x+half, y, half)
        quad(x+half, y+half, half)
        
            

    quad(0, 0, len(arr))
    return answer