def solution(s):
    stack = []
    
    for x in s:
        if stack:
            if stack[-1] == x:
                stack.pop()
                continue

        stack.append(x)
        
        
    return 0 if stack else 1