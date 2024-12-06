n, m = map(int, input().split())
res = []

def find_sequence():
    if len(res) == m:
        print(" ".join(map(str, res)))
        return 
    for i in range(1, n+1):         # 첫번째 숫자 기준 반복문
        if i not in res:
            res.append(i)
            find_sequence()
            res.pop()
            
find_sequence()