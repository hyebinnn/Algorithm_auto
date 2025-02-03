
n = int(input())
numbers = list(map(int, input().split()))
oper_count = list(map(int, input().split()))
ans_list = []

def dfs(ans, next_idx, oper_count):
    for i in range(4):
        if oper_count[i] > 0:
            if i == 0:           # + 일때
                ans += numbers[next_idx]
                oper_count[i] -= 1 
                dfs(ans, next_idx+1, oper_count)
                ans -= numbers[next_idx]
                oper_count[i] += 1 
            elif i == 1:
                ans -= numbers[next_idx]
                oper_count[i] -= 1 
                dfs(ans, next_idx+1, oper_count)
                ans += numbers[next_idx]
                oper_count[i] += 1 
            elif i == 2:
                ans *= numbers[next_idx]
                oper_count[i] -= 1 
                dfs(ans, next_idx+1, oper_count)
                ans = int(ans / numbers[next_idx])
                oper_count[i] += 1 
            elif i == 3:
                ans = int(ans / numbers[next_idx])
                oper_count[i] -= 1 
                dfs(ans, next_idx+1, oper_count)
                ans *= numbers[next_idx]
                oper_count[i] += 1 

    if sum(oper_count) == 0:
        ans_list.append(ans)

dfs(numbers[0], 1, oper_count)
print(max(ans_list))
print(min(ans_list))
