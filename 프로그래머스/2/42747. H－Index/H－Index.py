def solution(citations):
    mid = 0
    citations.sort(reverse=True)
    
    print(citations)
    
    while True:
        cnt = 0      # h번 이상 인용된 논문의 갯수
        for c in citations:
            if c >= mid:
                cnt += 1
            else:
                break
        
        if mid > cnt:
            break
            
        mid += 1
        
    return mid-1