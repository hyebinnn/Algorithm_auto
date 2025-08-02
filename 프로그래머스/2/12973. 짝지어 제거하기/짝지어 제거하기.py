def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
            continue
        stack.append(char)
        
    if stack:
        return 0
    return 1