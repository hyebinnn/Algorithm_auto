def solution(sides):
    sides.sort()
    cnt = 0
    for x in range(sides[1], 0, -1):
        if sides[0] + x > sides[1]:
            cnt += 1
        else:
            break
    for x in range(sides[1]+1, sides[0]+sides[1]):
        cnt += 1
        
    return cnt
    
    