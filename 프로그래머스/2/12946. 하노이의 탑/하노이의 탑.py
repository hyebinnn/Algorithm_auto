def solution(n):
    answer = []
    def hanoi(k, start, via, end):
        if k == 1:
            answer.append([start, end])
            return
        
        hanoi(k-1, start, end, via)
        answer.append([start, end])
        hanoi(k-1, via, start, end)
    
    hanoi(n, 1, 2, 3)
    return answer