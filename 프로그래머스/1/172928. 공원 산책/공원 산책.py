def solution(park, routes):
    direction = {
        "N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)
    }
    
    x=0
    y=0
    
    for i, p in enumerate(park):
        if "S" in p:
            x = i
            y = p.index("S")
            break

    for r in routes:
        d, num = r.split(" ")
        num = int(num)
        
        dx, dy = direction[d]
        
        if is_ok(park, dx, dy, x, y, num):
            x, y = x+(dx*num), y+(dy*num)
        
        
    return [x,y]
    
    
def is_ok(park, dx, dy, x, y, num):
    for _ in range(num):
        nx, ny = x+dx, y+dy

        if 0 <= nx < len(park) and 0<=ny<len(park[0]) and park[nx][ny] != "X":
            x, y = nx, ny
            continue
        else: 
            return False

    return True