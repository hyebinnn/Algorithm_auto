def solution(people, limit):
    people.sort()
    left, right = 0, len(people)-1
    cnt = 0
    while left <= right:
        if left == right:
            cnt += 1
            break
        if people[left] + people[right] <= limit:
            cnt += 1
            left += 1
            right -= 1
            continue
        cnt += 1
        right -= 1
    
    return cnt
            
    
#     people.sort()
#     visited = [0] * len(people)
#     cnt = 0 
#     for i in range(len(people)):
#         maxValue = 0
#         if not visited[i]: 
#             if people[i] > limit//2:
#                 cnt += 1
#                 visited[i] = 1
#                 continue
            
#             for j in range(i, len(people)):
#                 if not visited[j] and people[i] + people[j] <= limit:
#                     if maxValue <= people[i] + people[j]:
#                         maxIdx = j
#                         maxValue = people[i] + people[j]
#             visited[maxIdx] = 1
#             visited[i] = 1
#             cnt += 1
        
#     return cnt