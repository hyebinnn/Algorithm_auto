from itertools import combinations

def solution(nums):
    cnt = 0
    a = [sum(x) for x in list(combinations(nums, 3))]
    # print(a)
    for i in range(len(a)):
        for j in range(2, a[i]):
            if a[i] % j == 0:
                break
            elif a[i] % j != 0 and j == a[i] - 1:
                cnt += 1
        
    
    return cnt