import sys
input = sys.stdin.readline

n, k = map(int, input().split())
list_a = list(map(int, input().split()))


count = [0] * 100001
left, right = 0, 0
answer = 0
while right < n:
    if count[list_a[right]] >= k:
        count[list_a[left]] -= 1
        left += 1
    else:
        count[list_a[right]] += 1
        right += 1
    answer = max(answer, right - left)
    
print(answer)