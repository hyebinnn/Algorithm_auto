def is_correct(s):
    stack = []
    for ss in s:
        if ss == ")":
            if not stack:
                return False
            if stack[-1] == "(":
                stack.pop()
                continue
        
        stack.append(ss)
        
    return not(stack)
            
    

def solution(p):
    if p == "":
        return ""
    
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt == 0:
            u, v = p[:i+1], p[i+1:]
            break
            
    # 올바른 괄호라면
    if is_correct(u):
        return u + solution(v)
    else:
        temp = "("
        temp = temp + solution(v) + ")"
        u = list(u[1:len(u)-1])
        
        for i in range(len(u)):
            if u[i] == "(": 
                u[i] = ")"
            else:
                u[i] = "("
        
        temp += ''.join(u)
    
        return temp 
        