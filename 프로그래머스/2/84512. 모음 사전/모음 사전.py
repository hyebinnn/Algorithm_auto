def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    possible_words = []
    
    def dfs(current):
        if len(current) == len(alphabet):
            return
        
        for a in alphabet:
            possible_words.append(current+a)
            dfs(current+a)

    dfs("")
    possible_words.sort()
    return possible_words.index(word)+1