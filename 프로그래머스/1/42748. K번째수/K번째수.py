def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        temp = sorted(array[i-1:j])[k-1]
        answer.append(temp)
        
    return answer