from itertools import combinations

n = int(input())
people = list(i for i in range(n))
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

a = list(combinations(people, n//2))
start = a[:len(a)//2]
link = list(reversed(a[len(a)//2:]))

def get_skill(team):
    score = 0
    for i in range(len(team)-1):
        for j in range(i+1, len(team)):
            x, y = team[i], team[j]
            skill = board[x][y] + board[y][x]
            score += skill

    return score
        
res = 1000

for x in range(len(start)):
    skill_start = get_skill(start[x])
    skill_link = get_skill(link[x])
    res = min(res, abs(skill_start - skill_link))

print(res)