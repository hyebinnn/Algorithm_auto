def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    boat = 0
    
    while left < right:
        if people[left] + people[right] > limit:
            right -= 1      # 무거운 애 빼고 왼쪽으로 이동
        else: 
            right -= 1
            left += 1
            
        boat += 1
        
    return boat+1 if left == right else boat
        
        
        