def solution(numbers):
    N = len(numbers)
    result = []
    for i in range(N):
        for j in range(i+1, N):
            result.append(numbers[i]+numbers[j])
        
    return(sorted(set(result)))