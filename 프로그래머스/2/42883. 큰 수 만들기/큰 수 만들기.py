def solution(number, k):
    stack = []
    for n in number:
        while stack and k > 0:
            if stack[-1] >= n:
                break
            
            stack.pop()
            k -= 1
        
        stack.append(n)
            
    # 삭제 횟수가 남았다는건, 54321 이런 형태로 숫자가 계속 작아졌다는 점. 따라서 뒷자리부터 제거한다 k만큼
    if k > 0:
        stack = stack[:-k]
            
    return "".join(stack)