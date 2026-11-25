def solution(s):
    count = 0
    for ss in s:
        if ss == "(":
            count += 1
        else:
            count -= 1
        
        # 짝 없는 ) 가 처음으로 나오자마자 false return
        if count < 0:
            return False
    
    # count가 양수면 결과적으로 짝 없는 ( or 짝 없는 ) 존재
    return count == 0