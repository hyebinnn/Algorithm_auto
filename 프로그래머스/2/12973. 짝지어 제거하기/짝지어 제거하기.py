def solution(s):
    stack = []
    for ss in s:
        if stack and stack[-1] == ss:
            stack.pop()
            continue
        
        stack.append(ss)
        
    return 0 if stack else 1