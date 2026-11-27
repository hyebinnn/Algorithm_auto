def solution(n):
    answer = 0
    queens = [0] * n   # queens[r] = r행 퀸의 열 번호
    
    # 이 열에 놓아도 괜찮은지 테스트
    def is_safe(row, col):
        for r in range(row):
            # 모든 행의 퀸과 검사. 같은 열이라면 false
            if queens[r] == col:
                return False
            # 비교 대상 퀸의 위치가 현재 퀸의 대각선 위치라면 (두줄 위 대각선: (0,0) <-> (2,2))
            if abs(queens[r]-col) == abs(row-r):
                return False
            
        return True
                

    # 한 행의 퀸 열 위치 선정하는 함수
    def dfs(row):
        nonlocal answer
        
        # 무사히 마지막 행까지 돌았으면 answer 카운팅
        if row == n:
            answer += 1
            return
        
        # 어디 열에 놓을까?
        for col in range(n):
            if is_safe(row, col):
                queens[row] = col
                dfs(row+1)
        
        
                
    dfs(0)
    return answer
            
        
        
        