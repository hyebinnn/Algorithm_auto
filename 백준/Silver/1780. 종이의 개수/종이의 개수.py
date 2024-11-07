n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
count = [0, 0, 0]  

def divide(x, y, size):
    first_value = matrix[x][y]
    same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != first_value:
                same = False
                break
        if not same:
            break

    if same:
        count[first_value + 1] += 1 
    else:
        new_size = size // 3
        for i in range(3):
            for j in range(3):
                divide(x + i * new_size, y + j * new_size, new_size)

divide(0, 0, n)

print(count[0])  
print(count[1])  
print(count[2])  
