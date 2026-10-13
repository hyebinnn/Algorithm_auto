import math

def is_prime(number):
    if number < 2: 
        return False # 1이하는 소수가 아님
    
    for i in range(2, math.isqrt(number)+1):
        if number % i == 0:
            return False       # 나누어 떨어지면 소수가 아님
        
    return True
            

def solution(numbers):
    N = len(numbers)
    visited = [False] * N
    candidates = set()      # 011, 11 중복처리용
    
    def dfs(current):
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                candidates.add(int(current+numbers[i]))
                dfs(current+numbers[i])
                visited[i] = False
    
    dfs("")
    count = 0
    for c in candidates:
        count += is_prime(c)
        
    return count