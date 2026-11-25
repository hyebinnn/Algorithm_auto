from collections import defaultdict

def solution(nums):
    mon = defaultdict(int)
    count = len(nums) / 2
    
    for n in nums:
        mon[n] += 1
        
    if len(mon.keys()) > count:
        return count
    else:
        return len(mon.keys())