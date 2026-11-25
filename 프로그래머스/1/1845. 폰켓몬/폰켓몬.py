def solution(nums):
    kind = len(set(nums))
    count = len(nums) / 2
    
    return count if kind > count else kind