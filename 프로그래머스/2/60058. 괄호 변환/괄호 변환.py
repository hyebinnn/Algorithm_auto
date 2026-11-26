def is_correct(s):
    cnt = 0
    for ss in s:
        cnt += 1 if ss == "(" else -1
        if cnt < 0:
            return False
        
    return not cnt
            
            
    

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
        flipped = ''.join(")" if x == '(' else "(" for x in u[1:-1])
        temp = "(" + solution(v) + ")" + flipped
    
        return temp 
        